"""A moderately detailed Shiny for Python example application.

Run it with:
    shiny run --reload app.py

Install Shiny first if needed:
    python -m pip install shiny
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Literal

from shiny import App, Inputs, Outputs, Session, reactive, render, ui


Status = Literal["Backlog", "In Progress", "Review", "Done"]
Priority = Literal["Low", "Medium", "High"]

STATUSES: tuple[Status, ...] = ("Backlog", "In Progress", "Review", "Done")
PRIORITIES: tuple[Priority, ...] = ("Low", "Medium", "High")

STATUS_COLORS: dict[Status, str] = {
    "Backlog": "#64748b",
    "In Progress": "#2563eb",
    "Review": "#d97706",
    "Done": "#16a34a",
}
PRIORITY_COLORS: dict[Priority, str] = {
    "Low": "#16a34a",
    "Medium": "#d97706",
    "High": "#dc2626",
}


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


def seed_tasks() -> list[Task]:
    today = date.today()
    return [
        Task(1, "Sketch responsive dashboard layout", "Ari", "Done", "High", today - timedelta(days=3), 5, ["ui", "layout"]),
        Task(2, "Wire up project filters", "Blair", "In Progress", "Medium", today + timedelta(days=1), 3, ["forms"]),
        Task(3, "Add status distribution chart", "Casey", "Review", "Medium", today + timedelta(days=2), 2, ["chart"]),
        Task(4, "Write deployment checklist", "Devon", "Backlog", "Low", today + timedelta(days=7), 4, ["docs"]),
        Task(5, "Polish empty and validation states", "Ari", "In Progress", "High", today + timedelta(days=4), 6, ["ux"]),
        Task(6, "Review accessibility labels", "Casey", "Backlog", "Medium", today + timedelta(days=5), 3, ["a11y", "qa"]),
    ]


def status_badge(status: Status) -> ui.Tag:
    return ui.tags.span(
        status,
        class_="badge",
        style=f"--badge-color: {STATUS_COLORS[status]}",
    )


def priority_badge(priority: Priority) -> ui.Tag:
    return ui.tags.span(
        priority,
        class_="badge badge-outline",
        style=f"--badge-color: {PRIORITY_COLORS[priority]}",
    )


def tag_pill(tag: str) -> ui.Tag:
    return ui.tags.span(tag, class_="tag-pill")


app_ui = ui.page_fluid(
    ui.tags.style(
        """
        :root {
            --surface: #ffffff;
            --muted: #64748b;
            --line: #dbe3ef;
            --page: #f7f9fc;
            --text: #0f172a;
            --accent: #0f766e;
        }

        body {
            background: var(--page);
            color: var(--text);
        }

        .container-fluid {
            max-width: 1360px;
            padding: 24px;
        }

        .app-header {
            align-items: center;
            display: flex;
            gap: 16px;
            justify-content: space-between;
            margin-bottom: 18px;
        }

        .app-title h1 {
            font-size: 1.65rem;
            line-height: 1.2;
            margin: 0;
        }

        .app-title p {
            color: var(--muted);
            margin: 4px 0 0;
        }

        .layout {
            align-items: start;
            display: grid;
            gap: 16px;
            grid-template-columns: minmax(260px, 320px) 1fr;
        }

        .panel {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(15, 23, 42, 0.04);
            padding: 16px;
        }

        .panel h2,
        .panel h3 {
            font-size: 1rem;
            margin: 0 0 12px;
        }

        .sidebar-stack {
            display: grid;
            gap: 16px;
        }

        .metrics {
            display: grid;
            gap: 12px;
            grid-template-columns: repeat(5, minmax(120px, 1fr));
            margin-bottom: 16px;
        }

        .metric {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 14px;
        }

        .metric-label {
            color: var(--muted);
            font-size: 0.82rem;
        }

        .metric-value {
            font-size: 1.75rem;
            font-weight: 700;
            margin-top: 4px;
        }

        .content-stack {
            display: grid;
            gap: 16px;
        }

        .board {
            display: grid;
            gap: 12px;
            grid-template-columns: repeat(4, minmax(180px, 1fr));
        }

        .lane {
            background: #f8fafc;
            border: 1px solid var(--line);
            border-radius: 8px;
            min-height: 180px;
            padding: 12px;
        }

        .lane-header {
            align-items: center;
            display: flex;
            justify-content: space-between;
            margin-bottom: 10px;
        }

        .lane-title {
            font-weight: 700;
        }

        .lane-count {
            color: var(--muted);
            font-size: 0.85rem;
        }

        .task-card {
            background: var(--surface);
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            display: grid;
            gap: 8px;
            margin-top: 8px;
            padding: 12px;
        }

        .task-title {
            font-weight: 700;
            line-height: 1.35;
        }

        .task-meta {
            color: var(--muted);
            display: flex;
            flex-wrap: wrap;
            font-size: 0.86rem;
            gap: 8px 12px;
        }

        .badge {
            background: var(--badge-color);
            border: 1px solid var(--badge-color);
            border-radius: 999px;
            color: white;
            display: inline-block;
            font-size: 0.76rem;
            font-weight: 700;
            line-height: 1;
            padding: 5px 8px;
        }

        .badge-outline {
            background: transparent;
            color: var(--badge-color);
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
        }

        .tag-pill {
            background: #e2e8f0;
            border-radius: 999px;
            color: #334155;
            display: inline-block;
            font-size: 0.74rem;
            padding: 4px 8px;
        }

        .chart {
            display: grid;
            gap: 10px;
        }

        .bar-row {
            align-items: center;
            display: grid;
            gap: 10px;
            grid-template-columns: 110px 1fr 28px;
        }

        .bar-track {
            background: #e2e8f0;
            border-radius: 999px;
            height: 12px;
            overflow: hidden;
        }

        .bar-fill {
            background: var(--bar-color);
            height: 100%;
            width: var(--bar-width);
        }

        .task-table {
            border-collapse: collapse;
            width: 100%;
        }

        .task-table th,
        .task-table td {
            border-bottom: 1px solid var(--line);
            padding: 10px 8px;
            text-align: left;
            vertical-align: top;
        }

        .task-table th {
            color: #475569;
            font-size: 0.78rem;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }

        .empty-state {
            color: var(--muted);
            padding: 18px 0;
            text-align: center;
        }

        .form-note {
            color: var(--muted);
            font-size: 0.84rem;
            margin-top: 8px;
        }

        @media (max-width: 1100px) {
            .layout {
                grid-template-columns: 1fr;
            }

            .metrics,
            .board {
                grid-template-columns: repeat(2, minmax(180px, 1fr));
            }
        }

        @media (max-width: 680px) {
            .container-fluid {
                padding: 16px;
            }

            .app-header {
                align-items: flex-start;
                flex-direction: column;
            }

            .metrics,
            .board {
                grid-template-columns: 1fr;
            }
        }
        """
    ),
    ui.tags.div(
        ui.tags.div(
            ui.tags.h1("Shiny Project Board"),
            ui.tags.p("Reactive filters, KPI summaries, generated task lanes, and a small task-entry workflow."),
            class_="app-title",
        ),
        ui.input_action_button("reset_filters", "Reset filters", class_="btn-outline-secondary"),
        class_="app-header",
    ),
    ui.tags.div(
        ui.tags.aside(
            ui.tags.div(
                ui.tags.div(
                    ui.tags.h2("Filters"),
                    ui.input_text("query", "Search", placeholder="Title, owner, status, priority, or tag"),
                    ui.input_select("status_filter", "Status", ["All", *STATUSES], selected="All"),
                    ui.input_select("priority_filter", "Priority", ["All", *PRIORITIES], selected="All"),
                    ui.input_slider("max_hours", "Maximum estimate", min=1, max=12, value=12, step=1),
                    ui.input_checkbox("hide_done", "Hide completed work", value=False),
                    class_="panel",
                ),
                ui.tags.div(
                    ui.tags.h2("Add Task"),
                    ui.input_text("new_title", "Title", placeholder="Draft release notes"),
                    ui.input_text("new_owner", "Owner", placeholder="Ari"),
                    ui.input_select("new_status", "Status", STATUSES, selected="Backlog"),
                    ui.input_select("new_priority", "Priority", PRIORITIES, selected="Medium"),
                    ui.input_date("new_due", "Due date", value=(date.today() + timedelta(days=3)).isoformat()),
                    ui.input_numeric("new_estimate", "Estimate", value=2, min=1, max=12, step=1),
                    ui.input_text("new_tags", "Tags", placeholder="docs, release"),
                    ui.input_action_button("add_task", "Add task", class_="btn-primary"),
                    ui.output_ui("form_message"),
                    class_="panel",
                ),
                class_="sidebar-stack",
            ),
        ),
        ui.tags.main(
            ui.output_ui("metrics"),
            ui.tags.div(
                ui.tags.div(ui.tags.h2("Board"), ui.output_ui("board"), class_="panel"),
                ui.tags.div(ui.tags.h2("Status Distribution"), ui.output_ui("status_chart"), class_="panel"),
                ui.tags.div(ui.tags.h2("Task Table"), ui.output_ui("task_table"), class_="panel"),
                class_="content-stack",
            ),
        ),
        class_="layout",
    ),
)


def server(input: Inputs, output: Outputs, session: Session) -> None:
    tasks = reactive.Value(seed_tasks())
    message_text = reactive.Value("")

    @reactive.Calc
    def filtered_tasks() -> list[Task]:
        query = input.query().strip().lower()
        selected_status = input.status_filter()
        selected_priority = input.priority_filter()
        max_hours = input.max_hours()
        hide_done = input.hide_done()

        matches: list[Task] = []
        for task in tasks():
            searchable = " ".join(
                [
                    task.title,
                    task.owner,
                    task.status,
                    task.priority,
                    *task.tags,
                ]
            ).lower()
            if query and query not in searchable:
                continue
            if selected_status != "All" and task.status != selected_status:
                continue
            if selected_priority != "All" and task.priority != selected_priority:
                continue
            if task.estimate > max_hours:
                continue
            if hide_done and task.status == "Done":
                continue
            matches.append(task)
        return matches

    @reactive.Effect
    @reactive.event(input.reset_filters)
    def _reset_filters() -> None:
        ui.update_text("query", value="")
        ui.update_select("status_filter", selected="All")
        ui.update_select("priority_filter", selected="All")
        ui.update_slider("max_hours", value=12)
        ui.update_checkbox("hide_done", value=False)

    @reactive.Effect
    @reactive.event(input.add_task)
    def _add_task() -> None:
        title = input.new_title().strip()
        owner = input.new_owner().strip()
        if not title or not owner:
            message_text.set("Title and owner are required.")
            return

        current_tasks = tasks()
        next_id = max((task.id for task in current_tasks), default=0) + 1
        raw_due = input.new_due()
        due = raw_due if isinstance(raw_due, date) else date.fromisoformat(str(raw_due))
        tags = [tag.strip() for tag in input.new_tags().split(",") if tag.strip()]

        new_task = Task(
            id=next_id,
            title=title,
            owner=owner,
            status=input.new_status(),
            priority=input.new_priority(),
            due=due,
            estimate=int(input.new_estimate() or 1),
            tags=tags,
        )
        tasks.set([*current_tasks, new_task])
        message_text.set(f"Added task #{next_id}.")

        ui.update_text("new_title", value="")
        ui.update_text("new_owner", value="")
        ui.update_text("new_tags", value="")
        ui.update_numeric("new_estimate", value=2)

    @render.ui
    def form_message() -> ui.Tag:
        message = message_text()
        if not message:
            return ui.tags.span()
        return ui.tags.div(message, class_="form-note")

    @render.ui
    def metrics() -> ui.Tag:
        visible = filtered_tasks()
        completed = sum(task.status == "Done" for task in visible)
        open_hours = sum(task.estimate for task in visible if task.status != "Done")
        overdue = sum(task.due < date.today() and task.status != "Done" for task in visible)
        high_priority = sum(task.priority == "High" for task in visible)
        values = [
            ("Visible tasks", len(visible)),
            ("Completed", completed),
            ("Open hours", open_hours),
            ("Overdue", overdue),
            ("High priority", high_priority),
        ]
        return ui.tags.div(
            *[
                ui.tags.div(
                    ui.tags.div(label, class_="metric-label"),
                    ui.tags.div(str(value), class_="metric-value"),
                    class_="metric",
                )
                for label, value in values
            ],
            class_="metrics",
        )

    @render.ui
    def board() -> ui.Tag:
        visible = filtered_tasks()
        if not visible:
            return ui.tags.div("No tasks match the current filters.", class_="empty-state")

        lanes = []
        for status in STATUSES:
            lane_tasks = [task for task in visible if task.status == status]
            cards = [
                ui.tags.div(
                    ui.tags.div(task.title, class_="task-title"),
                    ui.tags.div(
                        ui.tags.span(f"Owner: {task.owner}"),
                        ui.tags.span(f"Due: {task.due.strftime('%b %d')}"),
                        ui.tags.span(f"{task.estimate}h"),
                        class_="task-meta",
                    ),
                    ui.tags.div(priority_badge(task.priority), *[tag_pill(tag) for tag in task.tags], class_="tag-row"),
                    class_="task-card",
                )
                for task in lane_tasks
            ]
            lanes.append(
                ui.tags.section(
                    ui.tags.div(
                        ui.tags.span(status, class_="lane-title"),
                        ui.tags.span(str(len(lane_tasks)), class_="lane-count"),
                        class_="lane-header",
                    ),
                    *cards,
                    class_="lane",
                )
            )
        return ui.tags.div(*lanes, class_="board")

    @render.ui
    def status_chart() -> ui.Tag:
        visible = filtered_tasks()
        counts = {status: sum(task.status == status for task in visible) for status in STATUSES}
        max_count = max(counts.values(), default=1) or 1
        rows = []
        for status, count in counts.items():
            rows.append(
                ui.tags.div(
                    ui.tags.div(status),
                    ui.tags.div(
                        ui.tags.div(
                            class_="bar-fill",
                            style=f"--bar-color: {STATUS_COLORS[status]}; --bar-width: {(count / max_count) * 100:.0f}%",
                        ),
                        class_="bar-track",
                    ),
                    ui.tags.div(str(count)),
                    class_="bar-row",
                )
            )
        return ui.tags.div(*rows, class_="chart")

    @render.ui
    def task_table() -> ui.Tag:
        visible = sorted(filtered_tasks(), key=lambda task: (task.status == "Done", task.due, task.priority))
        if not visible:
            return ui.tags.div("No rows to show.", class_="empty-state")

        header = ui.tags.tr(
            ui.tags.th("Task"),
            ui.tags.th("Owner"),
            ui.tags.th("Status"),
            ui.tags.th("Priority"),
            ui.tags.th("Due"),
            ui.tags.th("Hours"),
            ui.tags.th("Tags"),
        )
        rows = [
            ui.tags.tr(
                ui.tags.td(task.title),
                ui.tags.td(task.owner),
                ui.tags.td(status_badge(task.status)),
                ui.tags.td(priority_badge(task.priority)),
                ui.tags.td(task.due.isoformat()),
                ui.tags.td(str(task.estimate)),
                ui.tags.td(", ".join(task.tags) or "-"),
            )
            for task in visible
        ]
        return ui.tags.table(ui.tags.thead(header), ui.tags.tbody(*rows), class_="task-table")


app = App(app_ui, server)


if __name__ == "__main__":
    app.run()
