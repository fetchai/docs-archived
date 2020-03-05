The following functions help with diagnosing bugs and ensuring the correct state of variables and boolean tests.

## Panic

Force runtime errors with `panic()`. 

Use `panic` for unrecoverable states. When encountering the state, `panic()` terminates the program immediately providing feedback. 

``` c++
function main()

    var x = 1;
    var y = 2;
    var z = y + x;
    printLn(toString(z));
    z =- 2;
    if (z != -1)
    	panic("This is a terrible mistake!");
    endif
    printLn(toString(z));

endfunction
```

## Assert

Use `assert` to ensure state with optional feedback.


``` c++
function main()

    var x = 1;
    var y = 2;
    var z = y + x;
    printLn(toString(z));
    z =- 2;

    // assert(z == 1);
    assert(z == 1, "Feedback here.");

    printLn(toString(z));

endfunction
```


<br/>