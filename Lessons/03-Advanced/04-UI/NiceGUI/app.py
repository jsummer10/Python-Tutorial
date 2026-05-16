"""A moderately detailed NiceGUI example application.

Run it with:
    python app.py

Install NiceGUI first if needed:
    python -m pip install nicegui
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Literal

from nicegui import ui


Status = Literal["Backlog", "In Progress", "Review", "Done"]
Priority = Literal["Low", "Medium", "High"]


@dataclass
class Task:
    id: int
    title: str
    owner: str
    status: Status
    priority: Priority
    due: date
    estimate: int
    tags: list[str] = field(default_factory=list)


STATUS_COLORS: dict[Status, str] = {
    "Backlog": "grey-7",
    "In Progress": "blue-7",
    "Review": "orange-7",
    "Done": "green-7",
}
PRIORITY_COLORS: dict[Priority, str] = {
    "Low": "green-7",
    "Medium": "amber-8",
    "High": "red-7",
}

today = date.today()
tasks: list[Task] = [
    Task(1, "Sketch responsive dashboard layout", "Ari", "Done", "High", today - timedelta(days=3), 5, ["ui", "layout"]),
    Task(2, "Wire up project filters", "Blair", "In Progress", "Medium", today + timedelta(days=1), 3, ["forms"]),
    Task(3, "Add status distribution chart", "Casey", "Review", "Medium", today + timedelta(days=2), 2, ["chart"]),
    Task(4, "Write deployment checklist", "Devon", "Backlog", "Low", today + timedelta(days=7), 4, ["docs"]),
    Task(5, "Polish empty and validation states", "Ari", "In Progress", "High", today + timedelta(days=4), 6, ["ux"]),
]
next_task_id = max(task.id for task in tasks) + 1


def main() -> None:
    """Build the NiceGUI interface."""

    ui.colors(
        primary="#2563eb",
        secondary="#0f766e",
        accent="#f97316",
        positive="#16a34a",
        warning="#d97706",
        negative="#dc2626",
    )

    search_text = {"value": ""}
    status_filter = {"value": "All"}
    density = {"compact": False}

    task_rows = ui.column()
    board_columns: dict[Status, ui.column] = {}
    status_count_labels: dict[Status, ui.label] = {}
    table_container = ui.column()
    stats_row = ui.row()
    chart_container = ui.column()

    def filtered_tasks() -> list[Task]:
        query = search_text["value"].strip().lower()
        selected_status = status_filter["value"]

        result = []
        for task in tasks:
            searchable_text = " ".join([task.title, task.owner, task.status, task.priority, *task.tags]).lower()
            if query and query not in searchable_text:
                continue
            if selected_status != "All" and task.status != selected_status:
                continue
            result.append(task)
        return result

    def status_counts(items: list[Task]) -> dict[Status, int]:
        return {status: sum(task.status == status for task in items) for status in STATUS_COLORS}

    def priority_counts(items: list[Task]) -> dict[Priority, int]:
        return {priority: sum(task.priority == priority for task in items) for priority in PRIORITY_COLORS}

    def open_task_dialog(task: Task | None = None) -> None:
        is_editing = task is not None
        draft = task or Task(
            id=0,
            title="",
            owner="",
            status="Backlog",
            priority="Medium",
            due=today + timedelta(days=3),
            estimate=1,
            tags=[],
        )

        with ui.dialog() as dialog, ui.card().classes("w-[34rem] max-w-full gap-4"):
            ui.label("Edit task" if is_editing else "Add task").classes("text-xl font-semibold")

            title = ui.input("Title", value=draft.title).props("outlined dense").classes("w-full")
            owner = ui.input("Owner", value=draft.owner).props("outlined dense").classes("w-full")

            with ui.row().classes("w-full gap-3"):
                status = ui.select(list(STATUS_COLORS), label="Status", value=draft.status).props("outlined dense").classes("flex-1")
                priority = ui.select(list(PRIORITY_COLORS), label="Priority", value=draft.priority).props("outlined dense").classes("flex-1")

            with ui.row().classes("w-full gap-3"):
                due = ui.input("Due date", value=draft.due.isoformat()).props("outlined dense mask='####-##-##'").classes("flex-1")
                estimate = ui.number("Estimate (hours)", value=draft.estimate, min=1, max=40, step=1).props("outlined dense").classes("flex-1")

            tags = ui.input("Tags", value=", ".join(draft.tags), placeholder="ui, docs, api").props("outlined dense").classes("w-full")

            def save_task() -> None:
                global next_task_id

                cleaned_title = title.value.strip()
                cleaned_owner = owner.value.strip()
                if not cleaned_title or not cleaned_owner:
                    ui.notify("Title and owner are required", color="negative")
                    return

                try:
                    parsed_due = date.fromisoformat(due.value)
                except ValueError:
                    ui.notify("Use a valid due date in YYYY-MM-DD format", color="negative")
                    return

                values = {
                    "title": cleaned_title,
                    "owner": cleaned_owner,
                    "status": status.value,
                    "priority": priority.value,
                    "due": parsed_due,
                    "estimate": int(estimate.value or 1),
                    "tags": [tag.strip() for tag in tags.value.split(",") if tag.strip()],
                }

                if task is None:
                    tasks.append(Task(id=next_task_id, **values))
                    next_task_id += 1
                    ui.notify("Task added", color="positive")
                else:
                    for key, value in values.items():
                        setattr(task, key, value)
                    ui.notify("Task updated", color="positive")

                dialog.close()
                refresh()

            with ui.row().classes("w-full justify-end gap-2"):
                ui.button("Cancel", on_click=dialog.close).props("flat")
                ui.button("Save", icon="save", on_click=save_task).props("unelevated")

        dialog.open()

    def delete_task(task: Task) -> None:
        tasks.remove(task)
        ui.notify("Task deleted", color="warning")
        refresh()

    def move_task(task: Task, status: Status) -> None:
        task.status = status
        refresh()

    def render_task_card(task: Task) -> None:
        spacing = "gap-1 p-2" if density["compact"] else "gap-2 p-3"
        with ui.card().classes(f"w-full {spacing} rounded-lg shadow-sm"):
            with ui.row().classes("w-full items-start justify-between gap-2"):
                ui.label(task.title).classes("font-medium leading-snug")
                with ui.button(icon="more_vert").props("flat round dense").classes("shrink-0").tooltip("Task actions"):
                    with ui.menu():
                        ui.menu_item("Edit", lambda task=task: open_task_dialog(task))
                        ui.menu_item("Delete", lambda task=task: delete_task(task))

            with ui.row().classes("items-center gap-2 text-sm text-gray-600"):
                ui.icon("person").classes("text-base")
                ui.label(task.owner)
                ui.icon("event").classes("text-base ml-2")
                ui.label(task.due.strftime("%b %d"))

            with ui.row().classes("items-center gap-2"):
                ui.badge(task.priority, color=PRIORITY_COLORS[task.priority])
                for tag in task.tags[:3]:
                    ui.badge(tag, color="grey-3").classes("text-gray-800")

            with ui.row().classes("w-full items-center justify-between pt-1"):
                ui.label(f"{task.estimate}h estimate").classes("text-xs text-gray-500")
                with ui.button(icon="swap_horiz").props("flat dense").tooltip("Move task"):
                    with ui.menu():
                        for option in STATUS_COLORS:
                            ui.menu_item(option, lambda option=option, task=task: move_task(task, option))

    def render_board(items: list[Task]) -> None:
        for status, column in board_columns.items():
            column.clear()
            with column:
                for task in [item for item in items if item.status == status]:
                    render_task_card(task)

    def render_table(items: list[Task]) -> None:
        table_container.clear()
        with table_container:
            rows = [
                {
                    "id": task.id,
                    "title": task.title,
                    "owner": task.owner,
                    "status": task.status,
                    "priority": task.priority,
                    "due": task.due.isoformat(),
                    "estimate": task.estimate,
                    "tags": ", ".join(task.tags),
                }
                for task in items
            ]
            ui.table(
                columns=[
                    {"name": "title", "label": "Task", "field": "title", "align": "left", "sortable": True},
                    {"name": "owner", "label": "Owner", "field": "owner", "sortable": True},
                    {"name": "status", "label": "Status", "field": "status", "sortable": True},
                    {"name": "priority", "label": "Priority", "field": "priority", "sortable": True},
                    {"name": "due", "label": "Due", "field": "due", "sortable": True},
                    {"name": "estimate", "label": "Hours", "field": "estimate", "sortable": True},
                    {"name": "tags", "label": "Tags", "field": "tags", "align": "left"},
                ],
                rows=rows,
                row_key="id",
                pagination=8,
            ).classes("w-full").props("flat bordered")

    def render_stats(items: list[Task]) -> None:
        stats_row.clear()
        completed = sum(task.status == "Done" for task in items)
        total_hours = sum(task.estimate for task in items)
        overdue = sum(task.due < today and task.status != "Done" for task in items)
        review = sum(task.status == "Review" for task in items)
        stats = [
            ("Visible tasks", len(items), "fact_check", "primary"),
            ("Completed", completed, "task_alt", "positive"),
            ("In review", review, "rate_review", "warning"),
            ("Open hours", total_hours, "schedule", "secondary"),
            ("Overdue", overdue, "priority_high", "negative"),
        ]

        with stats_row:
            for label, value, icon, color in stats:
                with ui.card().classes("min-w-40 flex-1 gap-1 rounded-lg p-4"):
                    with ui.row().classes("items-center justify-between"):
                        ui.label(label).classes("text-sm text-gray-600")
                        ui.icon(icon).classes(f"text-{color}")
                    ui.label(str(value)).classes("text-3xl font-semibold")

    def render_chart(items: list[Task]) -> None:
        chart_container.clear()
        counts = status_counts(items)
        priorities = priority_counts(items)
        with chart_container:
            ui.echart(
                {
                    "tooltip": {"trigger": "axis"},
                    "legend": {"bottom": 0},
                    "grid": {"left": 24, "right": 16, "top": 20, "bottom": 52, "containLabel": True},
                    "xAxis": {"type": "category", "data": list(counts.keys())},
                    "yAxis": {"type": "value", "minInterval": 1},
                    "series": [
                        {
                            "name": "Tasks",
                            "type": "bar",
                            "data": list(counts.values()),
                            "itemStyle": {"color": "#2563eb"},
                        }
                    ],
                }
            ).classes("h-72 w-full")

            with ui.row().classes("w-full gap-2"):
                for priority, count in priorities.items():
                    ui.badge(f"{priority}: {count}", color=PRIORITY_COLORS[priority]).classes("text-sm px-3 py-2")

    def refresh() -> None:
        items = filtered_tasks()
        counts = status_counts(items)
        for status, label in status_count_labels.items():
            label.text = str(counts[status])
        render_stats(items)
        render_board(items)
        render_table(items)
        render_chart(items)

        task_rows.clear()
        with task_rows:
            if not items:
                with ui.card().classes("w-full items-center gap-2 rounded-lg p-6"):
                    ui.icon("search_off").classes("text-4xl text-gray-500")
                    ui.label("No tasks match the current filters.").classes("text-gray-600")

    ui.add_head_html(
        """
        <style>
            body { background: #f8fafc; }
            .nicegui-content { max-width: 1440px; margin: 0 auto; }
        </style>
        """
    )

    with ui.header(elevated=True).classes("items-center justify-between bg-white text-gray-900"):
        with ui.row().classes("items-center gap-3"):
            ui.icon("dashboard").classes("text-primary text-2xl")
            ui.label("NiceGUI Project Board").classes("text-lg font-semibold")
        with ui.row().classes("items-center gap-2"):
            ui.switch("Compact cards", value=False, on_change=lambda event: (density.update(compact=event.value), refresh()))
            ui.button("Add task", icon="add", on_click=lambda: open_task_dialog()).props("unelevated")

    with ui.column().classes("w-full gap-6 p-6"):
        with ui.row().classes("w-full items-end gap-3"):
            ui.input(
                "Search tasks",
                placeholder="Title, owner, status, priority, or tag",
                on_change=lambda event: (search_text.update(value=event.value), refresh()),
            ).props("outlined clearable debounce=250").classes("min-w-72 flex-1")
            ui.select(
                ["All", *STATUS_COLORS.keys()],
                label="Status",
                value="All",
                on_change=lambda event: (status_filter.update(value=event.value), refresh()),
            ).props("outlined").classes("w-56")

        stats_row.classes("w-full gap-3")

        with ui.tabs().classes("w-full") as tabs:
            board_tab = ui.tab("Board", icon="view_kanban")
            table_tab = ui.tab("Table", icon="table_chart")
            analytics_tab = ui.tab("Analytics", icon="monitoring")

        with ui.tab_panels(tabs, value=board_tab).classes("w-full bg-transparent"):
            with ui.tab_panel(board_tab).classes("p-0"):
                with ui.row().classes("w-full items-start gap-3"):
                    for status, color in STATUS_COLORS.items():
                        with ui.card().classes("min-w-64 flex-1 gap-3 rounded-lg p-3"):
                            with ui.row().classes("w-full items-center justify-between"):
                                ui.badge(status, color=color).classes("text-sm px-3 py-2")
                                status_count_labels[status] = ui.label("0").classes("text-sm text-gray-500")
                            board_columns[status] = ui.column().classes(
                                "w-full gap-2" if density["compact"] else "w-full gap-3"
                            )
                task_rows.classes("w-full")

            with ui.tab_panel(table_tab).classes("p-0"):
                table_container.classes("w-full")

            with ui.tab_panel(analytics_tab).classes("p-0"):
                with ui.card().classes("w-full rounded-lg p-4"):
                    ui.label("Work distribution").classes("text-lg font-semibold")
                    chart_container.classes("w-full")

    refresh()
    ui.run(title="NiceGUI Project Board", reload=False)


if __name__ in {"__main__", "__mp_main__"}:
    main()
