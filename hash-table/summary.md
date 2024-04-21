# Hash table

## Hash table
- Collection of items with **key value pairs**
- hash tables is implemented with **dictionary**

## Structure
- Each position is called **slot or bucket**

## Hash functions
- applied when it must return the **same value**for the **same input**
- Collisions: when the slot already has a value
    - must be solved

## Dictionary
- Denoted by {}
```python
my_dict = {}
```
- get() is used to get a key. if != something, return None
- items() used to get keys and values
- keys() used to get keys
- values() used to get values

## Inserting values
```python
my_dict = {}

my_dict['aidan'] = 18
```

## Modify values
```python
my_dict = {'aidan': 18}

my_dict['aidan'] = 19
```

## Delete pair
```python
my_dict = {'aidan': 19}

del my_dict['aidan']
```

## Clear a dict
my_dict.clear()