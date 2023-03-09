"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
import random

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    count = 0
    # count: int = 0

    # 증가 함수
    def increment(self):
        # self.count += 1
        self.count = self.count + 1

    # 감소
    def decrement(self):
        # self.count -= 1
        self.count = self.count - 1

    # 초기화 함수 (count state 값을 0 으로 초기화)
    def refresh(self):
        # self.count = self.count = 0
        self.count = 0

    # 랜덤 숫자 생성 함수
    def set_random(self):
        random_number = random.randrange(-1000, 1000)
        self.count = random_number


def index() -> pc.Component:
    return pc.center(
        pc.vstack(
            pc.heading("Welcome to Pynecone!", font_size="2em"),
            # State 값
            pc.heading(State.count, font_size="2em", color_scheme="blue"),
            # 감소 버튼
            pc.button(
                "감소",
                color_scheme="red",
                border_radius="1em",
                on_click=State.decrement,
            ),
            # 증가 버튼
            pc.button(
                "증가",
                color_scheme="green",
                border_radius="1em",
                on_click=State.increment,
            ),
            # 초기화 버튼
            pc.button("초기화", color_scheme="purple", border_radius="1em", on_click=State.refresh),
            # 랜덤 버튼
            pc.button("랜덤", color_scheme="blue", border_radius="1em", on_click=State.set_random),
        ),
    )


# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
