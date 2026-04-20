# Python Scope: Global vs Local Variables

## Method 1: Using the `global` Keyword

The `global` keyword tells Python: *"Don't create a new local variable; use the one that already exists in the global namespace."*

### How it works

```python
score = 0

def increase_score():
    global score  # Links the local name to the global variable
    score += 10   # Modifies the global variable directly

increase_score()
print(score)  # Output: 10
```

### Pros and Cons

**Pros:**
- Very direct
- Useful for simple scripts or "flag" variables that need to be accessed by many different functions

**Cons:**
- Harder to debug — if your global variable changes unexpectedly, you have to search every function that uses the `global` keyword to find the culprit
- Makes functions "impure" because they depend on things outside themselves

---

## Method 2: Using the `return` Statement

This is the **"functional" approach**. Instead of reaching out and grabbing the global variable, the function does its work and hands back the result to whoever called it.

### How it works

```python
score = 0

def calculate_new_score(current_score):
    return current_score + 10  # Returns a value, doesn't touch global scope

# We manually update the global variable with the returned value
score = calculate_new_score(score)
print(score)  # Output: 10
```

### Pros and Cons

**Pros:**
- Safer and more predictable
- The function is self-contained (a "Black Box")
- Easy to test because the output only depends on the input
- Standard practice in professional software development

**Cons:**
- Requires an extra step (re-assigning the variable)
- Can feel slightly more "wordy" for very simple tasks

---

## Summary Comparison

| Feature | `global` Keyword | `return` Statement |
|---|---|---|
| Side Effects | High (modifies external state) | None (contained within function) |
| Testing | Difficult (requires global setup) | Easy (just pass arguments) |
| Readability | Hidden (changes happen "behind the scenes") | Explicit (you see the assignment `x = func()`) |
| Best For | Small scripts, shared configurations | Complex logic, reusable libraries |

---

## Which One Should You Use?

In **90% of cases, use the `return` statement.** It keeps your code modular and prevents "spaghetti code" where variables are changing in ways that are hard to track.

The `global` keyword is generally considered a **"code smell"** — a sign that there might be a better way to structure the logic — in larger projects.



---

## Additional Concepts

### The LEGB Rule

Python looks up variable names in a specific order:

**Local → Enclosing → Global → Built-in**

This is the underlying reason why global/local scope behaves the way it does. It's worth knowing by name for the PCAP exam.

---

### Enclosing Scope (the "E" in LEGB)

When you have a function *inside* a function, the inner function can **read** the outer function's variables. Modifying them requires the `nonlocal` keyword — similar to `global`, but one level up.

```python
def outer():
    x = 10

    def inner():
        nonlocal x  # Refers to outer()'s x, not a global
        x += 5

    inner()
    print(x)  # Output: 15
```

---

### The Read vs. Modify Distinction

You can *read* a global variable from inside a function **without** the `global` keyword — Python will find it via LEGB. You only need `global` when you want to *reassign* it.

```python
score = 10

def show_score():
    print(score)  # Works fine — just reading, no global keyword needed

def reset_score():
    score = 0     # Creates a NEW local variable, does NOT touch the global!
```

> ⚠️ **Exam Trap:** `reset_score()` above does **not** change the global `score`. Python sees the assignment `score = 0` and creates a brand new local variable instead of modifying the global one. To actually reset the global, you would need `global score` at the top of the function.