To get started, set your OPENAI_API_KEY environment variable, or other required keys for the providers you selected.

Next, edit promptfooconfig.yaml.

Then run:
```
promptfoo eval
```

Afterwards, you can view the results by running `promptfoo view`

| Command             | Meaning                                | What it’s used for                     |
| ------------------- | -------------------------------------- | -------------------------------------- |
| `pip install build` | Installs the build tool                | Prepares for running `python -m build` |
| `python -m build`   | Builds your library                    | Generates the `dist/` folder           |
| `pip install -e .`  | Installs your library in editable mode | Use it locally while developing        |
