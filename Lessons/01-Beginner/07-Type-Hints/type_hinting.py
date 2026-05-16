"""
Comprehensive Python Type Hinting Examples
Covers built-ins, collections, generics, callables, protocols, and more.
"""

from __future__ import annotations

import sys
from collections.abc import Callable, Generator, Iterator, Sequence
from typing import (
    Annotated,
    Any,
    ClassVar,
    Final,
    Generic,
    Literal,
    NamedTuple,
    Never,
    Optional,
    Protocol,
    TypeAlias,
    TypeVar,
    TypedDict,
    Union,
    cast,
    overload,
    runtime_checkable,
)

# ---------------------------------------------------------------------------
# 1. PRIMITIVE / BUILT-IN TYPES
# ---------------------------------------------------------------------------

name: str = "Alice"
age: int = 30
height: float = 5.9
is_active: bool = True
raw_bytes: bytes = b"\x00\xff"
nothing: None = None


def greet(username: str, repeat: int = 1) -> str:
    return (f"Hello, {username}! " * repeat).strip()


# ---------------------------------------------------------------------------
# 2. COLLECTION TYPES  (use built-in generics; Python 3.9+)
# ---------------------------------------------------------------------------

scores: list[int] = [95, 87, 72]
coordinates: tuple[float, float] = (37.77, -122.41)
rgb: tuple[int, int, int] = (255, 128, 0)
variable_ints: tuple[int, ...] = (1, 2, 3, 4)   # homogeneous, any length

unique_ids: set[str] = {"abc", "def"}
frozen: frozenset[int] = frozenset({1, 2, 3})

phone_book: dict[str, str] = {"Alice": "555-1234"}
nested_map: dict[str, list[int]] = {"evens": [2, 4, 6], "odds": [1, 3, 5]}


# ---------------------------------------------------------------------------
# 3. OPTIONAL & UNION
# ---------------------------------------------------------------------------

# Optional[X] is shorthand for X | None
def find_user(user_id: int) -> Optional[str]:          # classic style
    return "Alice" if user_id == 1 else None


def divide(a: float, b: float) -> float | None:        # modern style (3.10+)
    return a / b if b != 0 else None


def process(value: int | str | bytes) -> str:           # multi-union
    return str(value)


# ---------------------------------------------------------------------------
# 4. LITERAL — restrict to specific values
# ---------------------------------------------------------------------------

Direction: TypeAlias = Literal["north", "south", "east", "west"]
StatusCode: TypeAlias = Literal[200, 201, 400, 404, 500]


def move(direction: Direction, steps: int = 1) -> str:
    return f"Moving {direction} {steps} step(s)."


def http_status(code: StatusCode) -> str:
    return f"HTTP {code}"


# ---------------------------------------------------------------------------
# 5. FINAL & CLASSVAR — constants and class-level attributes
# ---------------------------------------------------------------------------

MAX_RETRIES: Final[int] = 3
APP_NAME: Final = "MyApp"           # type inferred


class Config:
    instance_count: ClassVar[int] = 0
    debug: ClassVar[bool] = False

    def __init__(self, value: int) -> None:
        Config.instance_count += 1
        self.value: int = value


# ---------------------------------------------------------------------------
# 6. TYPE ALIASES
# ---------------------------------------------------------------------------

Vector: TypeAlias = list[float]
Matrix: TypeAlias = list[Vector]
JSON: TypeAlias = dict[str, "JSONValue"]          # forward reference
JSONValue: TypeAlias = str | int | float | bool | None | list["JSONValue"] | JSON


def dot_product(a: Vector, b: Vector) -> float:
    return sum(x * y for x, y in zip(a, b))


# ---------------------------------------------------------------------------
# 7. CALLABLE
# ---------------------------------------------------------------------------

Predicate: TypeAlias = Callable[[int], bool]
Transformer: TypeAlias = Callable[[str, int], str]


def apply_filter(numbers: list[int], pred: Predicate) -> list[int]:
    return [n for n in numbers if pred(n)]


def repeat_string(s: str, times: int) -> str:
    return s * times


def run_transform(fn: Transformer, text: str, n: int) -> str:
    return fn(text, n)


# Higher-order: returns a callable
def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiply(x: int) -> int:
        return x * factor
    return multiply


# ---------------------------------------------------------------------------
# 8. GENERICS & TYPEVARS
# ---------------------------------------------------------------------------

T = TypeVar("T")
K = TypeVar("K")
V = TypeVar("V")
Comparable = TypeVar("Comparable", int, float, str)  # constrained


def first(items: list[T]) -> T:
    return items[0]


def zip_to_dict(keys: list[K], values: list[V]) -> dict[K, V]:
    return dict(zip(keys, values))


def clamp(value: Comparable, lo: Comparable, hi: Comparable) -> Comparable:
    return max(lo, min(value, hi))


class Stack(Generic[T]):
    """A generic LIFO stack."""

    def __init__(self) -> None:
        self._items: list[T] = []

    def push(self, item: T) -> None:
        self._items.append(item)

    def pop(self) -> T:
        return self._items.pop()

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return not self._items

    def __len__(self) -> int:
        return len(self._items)


# ---------------------------------------------------------------------------
# 9. TYPED DICT — typed shapes for plain dicts
# ---------------------------------------------------------------------------

class Movie(TypedDict):
    title: str
    year: int
    rating: float


class ExtendedMovie(Movie, total=False):    # extra keys are optional
    director: str
    genres: list[str]


def summarise_movie(movie: Movie) -> str:
    return f"{movie['title']} ({movie['year']}) — {movie['rating']}/10"


# ---------------------------------------------------------------------------
# 10. NAMED TUPLE — immutable record with field names
# ---------------------------------------------------------------------------

class Point(NamedTuple):
    x: float
    y: float
    z: float = 0.0


class Employee(NamedTuple):
    name: str
    department: str
    salary: float


def distance(p1: Point, p2: Point) -> float:
    return ((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2) ** 0.5


# ---------------------------------------------------------------------------
# 11. PROTOCOL — structural subtyping ("duck typing" with types)
# ---------------------------------------------------------------------------

@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...


@runtime_checkable
class Sizeable(Protocol):
    def area(self) -> float: ...


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def draw(self) -> str:
        return f"○ (r={self.radius})"

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


class Square:
    def __init__(self, side: float) -> None:
        self.side = side

    def draw(self) -> str:
        return f"□ (side={self.side})"

    def area(self) -> float:
        return self.side ** 2


def render(shape: Drawable) -> None:
    print(shape.draw())


def total_area(shapes: Sequence[Sizeable]) -> float:
    return sum(s.area() for s in shapes)


# ---------------------------------------------------------------------------
# 12. ANNOTATED — attach metadata to a type
# ---------------------------------------------------------------------------

Positive    = Annotated[int, "must be > 0"]
Percentage  = Annotated[float, "0.0 - 100.0"]
NonEmptyStr = Annotated[str, "non-empty string"]


def set_volume(level: Percentage) -> str:
    assert 0.0 <= level <= 100.0
    return f"Volume set to {level}%"


def create_user(username: NonEmptyStr, age: Positive) -> dict[str, Any]:
    assert username, "username must not be empty"
    assert age > 0,  "age must be positive"
    return {"username": username, "age": age}


# ---------------------------------------------------------------------------
# 13. OVERLOAD — multiple signatures for one function
# ---------------------------------------------------------------------------

@overload
def double(x: int) -> int: ...
@overload
def double(x: str) -> str: ...
@overload
def double(x: list[T]) -> list[T]: ...

def double(x):                             # implementation (untyped body)
    if isinstance(x, list):
        return x + x
    return x + x                           # works for int, str, list


# ---------------------------------------------------------------------------
# 14. GENERATOR / ITERATOR
# ---------------------------------------------------------------------------

def fibonacci(limit: int) -> Generator[int, None, None]:
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def count_up(start: int, stop: int) -> Iterator[int]:
    current = start
    while current <= stop:
        yield current
        current += 1


# ---------------------------------------------------------------------------
# 15. NEVER & ANY — edge cases
# ---------------------------------------------------------------------------

def raise_error(msg: str) -> Never:
    """A function that never returns normally."""
    raise RuntimeError(msg)


def accept_anything(value: Any) -> Any:
    """Opts out of type checking entirely — use sparingly."""
    return value


# ---------------------------------------------------------------------------
# 16. CAST — tell the type checker "trust me"
# ---------------------------------------------------------------------------

def parse_id(raw: Any) -> int:
    return cast(int, int(raw))


# ---------------------------------------------------------------------------
# DEMO
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    # Primitives
    print(greet("World", 2))

    # Collections
    print(scores, coordinates, phone_book)

    # Optional / Union
    print(find_user(1), find_user(99))
    print(divide(10, 3), divide(10, 0))

    # Literal
    print(move("north", 3))

    # Generics
    stack: Stack[int] = Stack()
    stack.push(1); stack.push(2); stack.push(3)
    print(f"Stack peek: {stack.peek()}, size: {len(stack)}")

    # TypedDict
    film: Movie = {"title": "Inception", "year": 2010, "rating": 8.8}
    print(summarise_movie(film))

    # NamedTuple
    p1, p2 = Point(0, 0), Point(3, 4)
    print(f"Distance: {distance(p1, p2)}")

    # Protocol
    shapes: list[Circle | Square] = [Circle(5), Square(4)]
    for s in shapes:
        render(s)
    print(f"Total area: {total_area(shapes):.2f}")

    # Overload
    print(double(7), double("hi"), double([1, 2]))

    # Generator
    print(list(fibonacci(50)))

    # Annotated
    print(set_volume(75.0))
    print(create_user("alice", 25))