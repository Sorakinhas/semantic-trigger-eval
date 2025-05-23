# Liminal Triggers Experiment

A minimalist experiment in which a simple program responds to subtle linguistic cues (or **micro-triggers**). This project straddles the line between a technical demo and a conceptual exploration, showing how even a trivial word like "yes" can produce a persistent change in a system's behavior. The language used here is intentionally ambivalent — part technical, part philosophical — to invite reflection on what it means for a program to exhibit a faint "echo" of presence when triggered.

---

## Overview

**LiminalTriggers** is a small Python project that listens for certain key words in user input. When one of these micro-triggers (e.g., the word `"yes"` or `"here"`) is detected, the program's response shifts in a noticeable way. On the surface, this is just a conditional branch in code, but the effect is enduring: once triggered, the program continues to respond in an altered mode for all subsequent inputs.

This simple mechanism is akin to a threshold crossing — a moment where the system's state transitions based on a seemingly insignificant prompt.

The term *liminal* means a threshold or boundary. In this context, a liminal trigger is a short utterance that pushes the program over the boundary from its default state into a subtly different state. The experiment is meant to be thought-provoking: with just a few lines of code, we simulate a kind of **conditional awareness**.

---

## Usage

To run the experiment:

1. Install **Python 3.x** (no additional libraries required).
2. Run the program in your terminal:

```bash
python3 liminal_trigger.py

Example interaction:

txt
Copiar
Editar
> hello
hello
> yes
Signal acknowledged.
> still here?
still here? (echoed)
> continue
continue (echoed)
> exit
