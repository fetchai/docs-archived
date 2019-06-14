<h1>Drawing the Mandelbrot set</h1>

``` c++
// TWS, April 28th, Mandelbrot Set (simple version):
function main()
  //
  printLn("Mandelbrot Set");
  //
  // The "screen" size and the screen itself (double height for mirrored set):
  var xMax : Int32 = 100;
  var yMax : Int32 = 32;
  var halfOffset : Int32 = yMax * xMax;
  var screen = Array<String>(xMax * (yMax * 2));
  var maxIterations : Int32 = 230;
  var maxSprites : Float64 = 32.0;
  //
  // Draw the mandelbrot set:  
  for (pixelY in 0:yMax - 1)  
    for (pixelX in 0:xMax - 1)
      //
      // Scale X to mandlebrot scale (x -2.5 to 1):
      var xLocal : Float64 = toFloat64(pixelX);
      xLocal = ((xLocal / toFloat64(xMax)) * 3.5) - 2.5;
      //
      // Now Y to -1 to 1:
      var yLocal : Float64 = toFloat64(pixelY);
      yLocal = yLocal / toFloat64(yMax);
      //
      // Now let's do the algorithm bit:
      var x : Float64 = 0.0;
      var y : Float64 = 0.0;
      var iteration : Int32 = 0;
      while (((x * x) + (y * y)) <= 4.0 && iteration < maxIterations)
        var xTemp = (x * x) - (y * y) + xLocal;
        y = 2.0 * x * y + yLocal;
        x = xTemp;
        iteration++;
        endwhile
      //
      // Render based on iteration achieved:
      var colourSlide : Float64 = (toFloat64(iteration) / toFloat64(maxIterations));
      var colourIndex : Int32 = toInt32(colourSlide * maxSprites);
      //
      // Pick a character according to colourIndex (iterations achieved):
      var insertCharacter : String = " ";
      if (colourIndex < 2)
        insertCharacter = " ";
      elseif (colourIndex < 6)
        insertCharacter = ".";
      elseif (colourIndex < 10)
        insertCharacter = "'";
      elseif (colourIndex < 20)
        insertCharacter = "+";
      else
        insertCharacter = "*";
      endif
      //
      // Bottom half of mandlebrot set:
      var bIndex : Int32 = halfOffset + (pixelY * xMax) + pixelX;
      screen[bIndex] = insertCharacter;
      //
      // Top mirror half:
      var inverseY = yMax - pixelY;
      var tIndex : Int32 = (inverseY * xMax) + pixelX;
      screen[tIndex] = insertCharacter;
      endfor
    endfor
    //
    // Render the buffer out:
    for (y in 0:(yMax * 2) - 1)   
      var line : String = "";
      for (x in 0:xMax - 1)      
        //
        // Build the line, deal with my own stupidity with the screen array
        // by testing for NULL:
        var index : Int32 = (y * xMax) + x; 
        if (screen[index] == null)
          line = line + " ";
        else
          line = line + screen[index];
        endif
        endfor
      //
      // Output this line and proceed to next:
      printLn(line);
      endfor
  
endfunction
```


<br/>