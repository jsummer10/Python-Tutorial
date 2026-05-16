"""A moderately detailed Rich example application.

Run it with:
    python app.py

Install Rich first if needed:
    python -m pip install rich
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from time import sleep
from typing import Literal

from rich import box
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.markdown import Markdown
from rich.panel import Panel
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskProgressColumn, TextColumn, TimeElapsedColumn
from rich.rule import Rule
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text
from rich.tree import Tree


Status = Literal["Backlog", "In Progress", "Review", "Done"]
Priority = Literal["Low", "Medium", "High"]

STATUSES: tuple[Status, ...] = ("Backlog", "In Progress", "Review", "Done")
PRIORITIES: tuple[Priority, ...] = ("Low", "Medium", "High")

STATUS_STYLES: dict[Status, str] = {
    "Backlog": "slate_blue1",
    "In Progress": "dodger_blue2",
    "Review": "orange1",
    "Done": "green3",
}
PRIORITY_STYLES: dict[Priority, str] = {
    "Low": "green3",
    "Medium": "orange1",
    "High": "red1",
}


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    owner: str
    status: Status
    priority: Priority
    due: date
    estimate: int
    tags: list[str] = field(default_factory=list)


def seed_tasks() -> list[Task]:
    today = date.today()
    return [
        Task(1, "Sketch responsive dashboard layout", "Ari", "Done", "High", today - timedelta(days=3), 5, ["ui", "layout"]),
        Task(2, "Wire up project filters", "Blair", "In Progress", "Medium", today + timedelta(days=1), 3, ["forms"]),
        Task(3, "Add status distribution chart", "Casey", "Review", "Medium", today + timedelta(days=2), 2, ["chart"]),
        Task(4, "Write deployment checklist", "Devon", "Backlog", "Low", today + timedelta(days=7), 4, ["docs"]),
        Task(5, "Polish empty and validation states", "Ari", "In Progress", "High", today + timedelta(days=4), 6, ["ux"]),
        Task(6, "Review accessibility labels", "Casey", "Backlog", "Medium", today + timedelta(days=5), 3, ["a11y", "qa"]),
        Task(7, "Add production smoke test", "Devon", "Review", "High", today + timedelta(days=1), 4, ["release"]),
    ]


def count_by_status(tasks: list[Task]) -> dict[Status, int]:
    return {status: sum(task.status == status for task in tasks) for status in STATUSES}


def count_by_priority(tasks: list[Task]) -> dict[Priority, int]:
    return {priority: sum(task.priority == priority for task in tasks) for priority in PRIORITIES}


def build_header(tasks: list[Task]) -> Panel:
    complete = sum(task.status == "Done" for task in tasks)
    total_hours = sum(task.estimate for task in tasks)
    late_tasks = sum(task.due < date.today() and task.status != "Done" for task in tasks)

    title = Text("Rich Project Console", style="bold white")
    subtitle = Text(
        f"{len(tasks)} tasks | {complete} complete | {total_hours} estimated hours | {late_tasks} late",
        style="bright_black",
    )

    return Panel(
        Align.center(Group(title, subtitle), vertical="middle"),
        box=box.DOUBLE,
        border_style="cyan",
        padding=(1, 2),
    )


def build_metrics(tasks: list[Task]) -> Columns:
    status_counts = count_by_status(tasks)
    priority_counts = count_by_priority(tasks)
    total = len(tasks)
    done = status_counts["Done"]
    completion = round((done / total) * 100) if total else 0

    metric_values = [
        ("Completion", f"{completion}%", "green3" if completion >= 50 else "orange1"),
        ("Open Work", str(total - done), "dodger_blue2"),
        ("High Priority", str(priority_counts["High"]), "red1"),
        ("In Review", str(status_counts["Review"]), "orange1"),
    ]

    panels = []
    for label, value, style in metric_values:
        metric = Group(Text(value, style=f"bold {style}", justify="center"), Text(label, style="bright_black", justify="center"))
        panels.append(Panel(metric, box=box.ROUNDED, border_style=style, padding=(1, 2)))

    return Columns(panels, equal=True, expand=True)


def build_task_table(tasks: list[Task]) -> Table:
    table = Table(title="Delivery Board", box=box.SIMPLE_HEAVY, expand=True, row_styles=["", "dim"])
    table.add_column("ID", justify="right", style="bright_black", no_wrap=True)
    table.add_column("Task", style="white")
    table.add_column("Owner", no_wrap=True)
    table.add_column("Status", no_wrap=True)
    table.add_column("Priority", no_wrap=True)
    table.add_column("Due", no_wrap=True)
    table.add_column("Estimate", justify="right", no_wrap=True)
    table.add_column("Tags", style="bright_black")

    for task in sorted(tasks, key=lambda item: (item.status == "Done", item.due, item.priority)):
        due_style = "red1" if task.due < date.today() and task.status != "Done" else "white"
        table.add_row(
            str(task.id),
            task.title,
            task.owner,
            Text(task.status, style=STATUS_STYLES[task.status]),
            Text(task.priority, style=PRIORITY_STYLES[task.priority]),
            Text(task.due.strftime("%b %d"), style=due_style),
            f"{task.estimate}h",
            ", ".join(task.tags),
        )

    return table


def build_board_tree(tasks: list[Task]) -> Tree:
    tree = Tree("[bold]Workflow[/bold]")

    for status in STATUSES:
        branch = tree.add(f"[{STATUS_STYLES[status]}]{status}[/{STATUS_STYLES[status]}]")
        for task in [item for item in tasks if item.status == status]:
            tag_text = ", ".join(f"[bright_black]{tag}[/bright_black]" for tag in task.tags)
            branch.add(f"{task.title} ([bold]{task.owner}[/bold], {task.estimate}h) {tag_text}")

    return tree


def build_priority_table(tasks: list[Task]) -> Table:
    table = Table(title="Priority Mix", box=box.MINIMAL_DOUBLE_HEAD, expand=True)
    table.add_column("Priority")
    table.add_column("Tasks", justify="right")
    table.add_column("Hours", justify="right")

    for priority in PRIORITIES:
        items = [task for task in tasks if task.priority == priority]
        table.add_row(
            Text(priority, style=PRIORITY_STYLES[priority]),
            str(len(items)),
            f"{sum(task.estimate for task in items)}h",
        )

    return table


def build_markdown_panel() -> Panel:
    markdown = Markdown(
        """
### Release Notes

- Use `Table` for dense operational data.
- Use `Tree` when hierarchy matters.
- Use `Progress` for long-running jobs.
- Use `Syntax` to render code with highlighting.
"""
    )
    return Panel(markdown, title="Markdown", border_style="magenta", box=box.ROUNDED)


def build_syntax_panel() -> Panel:
    code = """\
def overdue(tasks: list[Task]) -> list[Task]:
    today = date.today()
    return [
        task
        for task in tasks
        if task.due < today and task.status != "Done"
    ]
"""
    syntax = Syntax(code, "python", theme="monokai", line_numbers=True, word_wrap=True)
    return Panel(syntax, title="Syntax Highlighting", border_style="green3", box=box.ROUNDED)


def run_deployment_preview(console: Console, tasks: list[Task]) -> None:
    console.log("Starting simulated release checks")

    steps = [
        ("Lint project files", 24),
        ("Run unit tests", 38),
        ("Build terminal report", 30),
        ("Publish dry run", 18),
    ]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=console,
    ) as progress:
        progress_tasks = [progress.add_task(label, total=total) for label, total in steps]
        while not all(progress.tasks[index].finished for index in range(len(progress_tasks))):
            for task_id in progress_tasks:
                if not progress.tasks[task_id].finished:
                    progress.advance(task_id)
            sleep(0.015)

    blocked = [task for task in tasks if task.priority == "High" and task.status != "Done"]
    if blocked:
        console.log(f"{len(blocked)} high-priority tasks remain before release", style="bold orange1")
    else:
        console.log("No high-priority tasks remain before release", style="bold green3")


def main() -> None:
    console = Console()
    tasks = seed_tasks()

    console.clear()
    console.print(build_header(tasks))
    console.print()
    console.print(build_metrics(tasks))
    console.print()
    console.print(build_task_table(tasks))
    console.print()
    console.print(
        Columns(
            [
                Panel(build_board_tree(tasks), title="Grouped Tree", border_style="cyan", box=box.ROUNDED),
                build_priority_table(tasks),
            ],
            equal=True,
            expand=True,
        )
    )
    console.print()
    console.print(Columns([build_markdown_panel(), build_syntax_panel()], equal=True, expand=True))
    console.print()
    console.print(Rule("Simulated Work"))
    run_deployment_preview(console, tasks)
    console.print()
    console.print(Panel.fit("[bold green]Rich demo complete[/bold green]", border_style="green3"))


if __name__ == "__main__":
    main()
