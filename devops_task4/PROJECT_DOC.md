# DevOps Task 4 - Git Workflow Documentation

## Branching Strategy
- **main** → Production-ready code
- **dev** → Integration branch for tested code
- **feature/** → New features or fixes

## Workflow
1. Create a feature branch from `dev`
2. Commit changes frequently
3. Push to GitHub
4. Open a Pull Request to `dev`
5. After testing, merge `dev` into `main`

## Tools Used
- Git
- GitHub

## Tags
- v1.0 → First stable release

## .gitignore Purpose
Prevents tracking of unnecessary files like:
- Build files
- Logs
- Environment variables
