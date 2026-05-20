# CodSpeed

## Project

[https://github.com/CodSpeedHQ/codspeed](https://github.com/CodSpeedHQ/codspeed)

## What It Is

CodSpeed is a continuous benchmarking platform designed to track application performance directly within your CI/CD pipeline (like GitHub Actions).

Traditionally, measuring code speed in the cloud is a nightmare. Cloud virtual machines share hardware, meaning your benchmarks might swing by 10% to 20% from one minute to the next just because of background noise. CodSpeed fixes this by using a deterministic CPU simulator. Instead of timing how many seconds your code takes to run, it counts the exact number of CPU instructions it executes.

The result? Performance metrics with less than 1% variance, making your benchmarks completely stable and reproducible.

## What It's Used For

- Catching Performance Regressions: It acts as a gatekeeper for your code. If a developer opens a Pull Request that introduces a massive, accidental slowdown in a core function, CodSpeed catches it before that code ever hits production.
- Differential Flame Graphs: When your code does slow down, it doesn't just give you a vague warning. It generates a visual map (a flame graph) comparing the old code to the new code, pointing you directly to the exact lines of code causing the bottleneck.
- Performance Tracking Over Time: It provides a dashboard that maps your project's performance history across branches, helping you see if your software is getting leaner or more bloated over months of development.

## Demo

[https://github.com/CodSpeedHQ/pyconus-2026-tutorial](https://github.com/CodSpeedHQ/pyconus-2026-tutorial)
