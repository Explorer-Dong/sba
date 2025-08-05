## project frame

- cdm: pretrained model
- data: test data and context info
- utils: some tool functions
    - graph: graph function
    - llm_api: agent function
- config: global config
- sba_baseline: baseline module
- sba_ours: our algorithm
- validate_downstream1 & 2: validate downstream task
- validate_hypothesis: validate initial hypothesis

## how to run

- mkdir:

    ```bash
    mkdir outputs
    ```

- create llm api:

    ```bash
    touch .env
    echo > <your llm api>
    ```

- run and validate:

    ```bash
    python -m sba_baseline.py
    python -m sba_ours.py
    ```

    then, all results will appear in `outputs` folder and console.
