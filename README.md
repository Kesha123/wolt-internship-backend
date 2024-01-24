# Delivery Fee Calculator Backend

## Background
This application is needed when a customer is ready with their shopping cart and they’d like to see how much the delivery will cost. The delivery price depends on the cart value, the number of items in the cart, the time of the order, and the delivery distance.

## Desciption

## Requirements

## Installation

## How to run
You are very flexible in a choice of the way you want to run the application.

You can run with:

1. **Docker**
    - [ ] Build the image first
    ```
    docker build -t delivery-fee-calculator -f Dockerfile.development .
    ```
    - [ ] Run **"production"** container
    ```
    docker run -d --rm -p 8080:8080 --name delivery-fee-calculator delivery-fee-calculator
    ```
    - [ ] Or run **development** container. Dont forget to change `/path/to/wolt-internship-backend/` to your actual path
    ```
    docker run -d --rm -p 8080:8080 --name delivery-fee-calculator -v "/path/to/wolt-internship-backend/src:/app/src" delivery-fee-calculator
    ```

2. **Basic command line**
    ```
    python3 src/main.py
    ```

If application was run successfuly you will see the following output
```
==============================
Server is running on port 8080
==============================
```

## How to test

Test set-up consists of:
1. Calculator and its functions itsef testing.
2. Calculator endpoint testing.
3. Backend general health testing.

Data needed for tests (fixtures) is stored in `tests/conftest.py`

You can run test with the following command.
```
pytest tests/
```

If you'd like to run a particular set of tests, you can specify the desired file
```
pytest tests/tests/test_api_health.py
```

If you'd like to tetst a particular method, you can specify it like this
```
pytest tests/test_calculator.py::test_small_order_surcharge
```

You can add `--verbose` *or* `-v` to see detailed output
```
pytest tests/ --verbose
```


## Documentation
Along with the application itself, Swagger documentation is provided. It can be accessed with this link: **[Swagger Backend Documentation](http://localhost:8080/api/doc/)**

Or you can navigate to http://localhost:8080/api/doc/ in your browser.