<h1>Drawing the Fetch logo</h1>

``` c++
function main()
  //
  printLn("Hello, everyone. Let's do some drawing.");
  //
  // Some messing about to test something; the for range of 0:0 (start/end) means we 
  // can't *not* iterate, which is worthy of discussion.
  for (i in 0:0)
//    printLn("A-TEST: Wish we didn't see this - " + toString(i));
    endfor
  for (i in 0:1)
//    printLn("B-TEST: And this should be once, but it's twice - " + toString(i));
    endfor
  //
  // Declare logo array (for string building) and the starting values:
  var fetchLogo = Array<Int32>(64 * 64);
  var leftAmount : Int32 = 60;
  var rightAmount : Int32 = 0;
  //
  // Flip flop does an aspect ratio correction if enabled:
  var flipFlop : Bool = false;
  var enableFlipFlop : Bool = true;  
  for (y in 0:63)
    //
    // Reset the array line, then add left and right with space between:
    for (i in 0:63)
      fetchLogo[i] = 0;
      endfor
    
    for (leftBit in 0:leftAmount)   
      fetchLogo[leftBit] = 1;
      endfor
      
    var cursor = leftAmount + 3;
    for (rightBit in 0:rightAmount)  // -- see discussion point in header
      fetchLogo[cursor + rightBit] = 1;
      endfor  
    //
    // Adjust for next line:
    leftAmount--;
    rightAmount++;
    //
    // Now render the line, skipping every other if we're in that
    // mode:
    if (false == enableFlipFlop || (enableFlipFlop && flipFlop))
      var logoLine : String = "";
      for (stringIndex in 0:63)    
        if (0 == fetchLogo[stringIndex])
          logoLine = logoLine + " ";
        else
          logoLine = logoLine + "*";
          endif       
        endfor
    
      printLn(logoLine);      
      endif
    //
    // Invert flipflop for next iteration:
    flipFlop = !flipFlop;
    endfor
  
endfunction
```

<br/>