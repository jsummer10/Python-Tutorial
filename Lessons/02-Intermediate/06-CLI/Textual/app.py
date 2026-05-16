"""A small sample Textual application.

Run it with:
    python cli_utils.py

Install Textual first if needed:
    python -m pip install textual
"""

from __future__ import annotations

from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.reactive import reactive
from textual.widgets import Button, Footer, Header, Input, Label, ListItem, ListView, Static


class TaskItem(ListItem):
    """A selectable task row."""

    def __init__(self, description: str, done: bool = False) -> None:
        super().__init__()
        self.description = description
        self.done = done

    def compose(self) -> ComposeResult:
        marker = "[x]" if self.done else "[ ]"
        yield Label(f"{marker} {self.description}", classes="done" if self.done else "")

    def toggle(self) -> None:
        self.done = not self.done
        self.refresh(recompose=True)


class Summary(Static):
    """Shows basic task totals."""

    total = reactive(0)
    done = reactive(0)

    def render(self) -> str:
        remaining = self.total - self.done
        return f"Total: {self.total} | Done: {self.done} | Remaining: {remaining}"


class TaskApp(App):
    """Simple Textual app for collecting and checking off tasks."""

    CSS = """
    Screen {
        layout: vertical;
    }

    #main {
        height: 1fr;
        padding: 1 2;
    }

    #entry {
        height: auto;
        margin-bottom: 1;
    }

    #task-input {
        width: 1fr;
    }

    #add-button {
        width: 12;
        margin-left: 1;
    }

    #task-list {
        border: solid $primary;
        height: 1fr;
    }

    Summary {
        dock: bottom;
        height: 3;
        content-align: center middle;
        background: $surface;
    }

    .done {
        color: $success;
        text-style: strike;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("a", "focus_input", "Add task"),
        ("space", "toggle_selected", "Toggle done"),
        ("d", "delete_selected", "Delete"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Vertical(id="main"):
            yield Label("Textual Task Board")
            with Horizontal(id="entry"):
                yield Input(placeholder="Type a task and press Enter", id="task-input")
                yield Button("Add", id="add-button", variant="primary")
            yield ListView(
                TaskItem("Install Textual"),
                TaskItem("Run this sample app"),
                TaskItem("Add your own task"),
                id="task-list",
            )
        yield Summary()
        yield Footer()

    def on_mount(self) -> None:
        self.title = "Textual Task Board"
        self.sub_title = "A tiny CLI user interface"
        self.query_one("#task-input", Input).focus()
        self.update_summary()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        if event.input.id == "task-input":
            self.add_task(event.value)
            event.input.value = ""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-button":
            task_input = self.query_one("#task-input", Input)
            self.add_task(task_input.value)
            task_input.value = ""
            task_input.focus()

    def action_focus_input(self) -> None:
        self.query_one("#task-input", Input).focus()

    def action_toggle_selected(self) -> None:
        task_list = self.query_one("#task-list", ListView)
        selected = task_list.highlighted_child
        if isinstance(selected, TaskItem):
            selected.toggle()
            self.update_summary()

    def action_delete_selected(self) -> None:
        task_list = self.query_one("#task-list", ListView)
        selected = task_list.highlighted_child
        if selected is not None:
            selected.remove()
            self.update_summary()

    def add_task(self, task: str) -> None:
        task = task.strip()
        if not task:
            return

        task_list = self.query_one("#task-list", ListView)
        task_list.append(TaskItem(task))
        self.update_summary()

    def update_summary(self) -> None:
        tasks = list(self.query(TaskItem))
        summary = self.query_one(Summary)
        summary.total = len(tasks)
        summary.done = sum(task.done for task in tasks)


def main() -> None:
    app = TaskApp()
    app.run()


if __name__ == "__main__":
    main()
