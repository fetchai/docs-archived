## The most basic introduction

`etch` is a high-level, statically-typed programming language designed for creating smart contracts on the Fetch.AI constellation ledger. Unlike similar languages, `etch` allows developers to code advanced compute-intensive logic for high performance scenarios such as machine learning and AI.

Check out the Fetch.AI `etch` language guide <a href="https://docs.fetch.ai/etch-language/" target=_blank>here</a>.

But for the quickest start...

## Hello World
    
``` c++
function main()
  for (i in 0:5)
    printLn("Hello World, how are you? (" + toString(i) + ")");
  endfor
endfunction
```
  
Copy/paste the code into the window on the left. Click run and you will see the results in the right.

The `main` function is where execution starts. The `for` loop prints out “Hello world” along with a number representing the loop index.

## Flow control and looping

As well as `for`, `etch` also supports `while`:

``` c++
function main()
  var i : Int32 = 0;
  while (i < 10)
    printLn(toString(i));
    i++;
  endwhile
endfunction
```
    
`for` and `while` support `continue` and `break` which skip an iteration or break out of the loop respectively.

Note that we support `++` for increment. We also support operators for `+=`, `--`, `-=`, etc. Also observe that we declare the variable `i` as an `Int32` a 32 bit integer type. `etch` has many built-in types, and they include: `Float32`, `Float64`, `Int32`, `Int64`, `UInt32`, `UInt64`, `Bool`, `String`, `Array`, and more.

For flow control, use the `if/else/elseif/endif` structure:

``` c++
function main()
  var colourIndex = 15;
  var insertCharacter : String = " ";
  if (colourIndex < 2)
    insertCharacter = " ";
  elseif (colourIndex < 8)
    insertCharacter = "'";
  elseif (colourIndex < 20)
    insertCharacter = "*";
  else
    insertCharacter = "@";
  endif
  printLn(insertCharacter);
endfunction
```           

Check out <a href="https://docs.fetch.ai/etch-language/" target=_blank>the guide</a> for further details, including information on complex data structures and smart contract creation.

