<!-- commenting out TrainingPair for now -->
<!-- currently, 29/10/19, the implementation below is out of date -->

`TrainingPair` is a custom `etch` class used to load data into a `DataLoader`. 

A `TrainingPair` contains pairs of training data and the corresponding training label coming from two `Tensor` types.

Declare and initialise a `TrainingPair`.

``` c++
function main()
	
	var trainingPair = TrainingPair(tensor1, tensor2);

endfunction
```

The code below builds two `Tensor` types, then creates a `TrainingPair` type with them.

``` c++
function main()

    var shape = Array<UInt64>(2);
    shape[0] = 28u64;
    shape[1] = 28u64;
    var tensor1 = Tensor(shape);

    shape[0] = 1u64;
    shape[1] = 10u64;
    var tensor2 = Tensor(shape);

    var trainingPair = TrainingPair(tensor1, tensor2);

endfunction
```



<br/>