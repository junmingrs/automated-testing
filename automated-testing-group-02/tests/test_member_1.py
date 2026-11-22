from os import name

import pytest
from playwright.sync_api import Page, expect

URL = "https://demo.playwright.dev/todomvc/"


def test_add_task(page: Page):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")
    task_labels = task_items.locator("label")

    expect(task_items).to_have_count(0)

    task_input.fill("Read testing notes")
    task_input.press("Enter")

    expect(task_items).to_have_count(1)
    expect(task_labels).to_have_text(["Read testing notes"])
    expect(task_input).to_have_value("")

def test_complete_task(page: Page):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    task_input.fill("Practise automated testing")
    task_input.press("Enter")

    expect(task_items).to_have_count(1)

    checkbox = task_items.first.get_by_role("checkbox")
    checkbox.check()
    expect(checkbox).to_be_checked()

    page.get_by_role("link", name="Completed", exact=True).click()

    expect(task_items).to_have_count(1)
    expect(task_items.locator("label")).to_have_text(
        ["Practise automated testing"]
    )

@pytest.mark.parametrize(
    "task_text",
    ["", " ", "   "],
    ids=["empty", "one-space", "three-spaces"],
)
def test_blank_task_is_not_added(page: Page, task_text: str):
    page.goto(URL)

    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    task_input.fill(task_text)
    task_input.press("Enter")

    expect(task_items).to_have_count(0)

def test_login_with_correct_details(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_role(
            "heading",
            name="Secure Area",
            exact=True,
        )
    ).to_be_visible()

def test_login_with_incorrect_password(page: Page):
    page.goto("https://the-internet.herokuapp.com/login")

    page.get_by_label("Username").fill("tomsmith")
    page.get_by_label("Password").fill("WrongPassword123")
    page.get_by_role("button", name="Login").click()

    expect(
        page.get_by_text("Your password is invalid!")
    ).to_be_visible()

    expect(
        page.get_by_role("button", name="Login")
    ).to_be_visible()

def add_task(page: Page, task_name: str):
    task_input = page.get_by_placeholder(
        "What needs to be done?",
        exact=True,
    )
    task_input.fill(task_name)
    task_input.press("Enter")

def test_add_two_tasks(page: Page):
    page.goto(URL)
    task_items = page.locator(".todo-list li")

    expect(task_items).to_have_count(0)

    add_task(page, "Read the instructions")
    add_task(page, "Practise the examples")

    expect(task_items).to_have_count(2)
    expect(task_items.locator("label")).to_have_text(
        ["Read the instructions", "Practise the examples"]
    )

def test_active_filter_shows_unfinished_task(page: Page):
    page.goto(URL)

    # Add your setup and actions.
    add_task(page, "A fictional task")
    task_items = page.locator(".todo-list li")
    checkbox = task_items.first.get_by_role("checkbox")
    checkbox.check()
    page.get_by_role("link", name="Completed", exact=True).click()

    # Add meaningful assertions.
    expect(checkbox).to_be_checked()
    expect(task_items).to_have_count(1)
    expect(task_items.locator("label")).to_have_text(["A fictional task"])

    # Capture your final PNG after the assertions.
    page.screenshot(
    path="docs/evidence/member-1/extra-test-1-active-filter.png",
    full_page=True,
    )

def test_delete_task(page: Page):
    page.goto(URL)

    # Add your setup and actions.
    add_task(page, "A fictional task")
    task_items = page.locator(".todo-list li")
    task_items.hover()
    delete_button = task_items.first.get_by_role("button", name="Delete")
    delete_button.click()

    # Add meaningful assertions.
    expect(delete_button).to_be_hidden()

    # Capture your final PNG after the assertions.
    page.screenshot(
    path="docs/evidence/member-1/extra-test-2-delete-task.png",
    full_page=True,
    )


def test_edit_existing_task(page: Page):
    page.goto(URL)
    add_task(page, "Complete assignment")

    task = page.locator(".todo-list li")
    task.locator("label").dblclick()

    edit_field = task.locator(".edit")
    edit_field.fill("Complete DevOps assignment")
    edit_field.press("Enter")

    expect(task.locator("label")).to_have_text(
        "Complete DevOps assignment"
    )
    expect(page.get_by_text(
        "Complete assignment", exact=True
    )).to_have_count(0)

    page.screenshot(
        path="docs/evidence/member-1/extra-test-1-edit.png",
        full_page=True
    )


def test_clear_completed_tasks(page: Page):
    page.goto(URL)

    add_task(page, "Task A")
    add_task(page, "Task B")
    add_task(page, "Task C")

    tasks = page.locator(".todo-list li")
    expect(tasks).to_have_count(3)

    tasks.nth(0).locator(".toggle").check()
    tasks.nth(1).locator(".toggle").check()

    page.get_by_role(
        "button", name="Clear completed"
    ).click()

    expect(tasks).to_have_count(1)
    expect(tasks.locator("label")).to_have_text(
        ["Task C"]
    )
    expect(tasks.locator(".toggle")).not_to_be_checked()

    page.screenshot(
        path="docs/evidence/member-1/extra-test-2-clear.png",
        full_page=True
    )


