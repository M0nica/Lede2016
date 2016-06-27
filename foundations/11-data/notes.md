## How to get PDF Data into .CSV

### Copy/Pasted content of PDF.

We are only interested in the lines that begin with 3 digits.

Then used find and replace in atom on "^[^\d].*" in order to select all lines that did not begin with a digit. Then replaced all of these unecessary lines with blankness.Be sure to turn on regex's first.


Then found all of the commas and replaced them with nothing.


### Saved parsed file as .CSV

'(\d\d\d)\s+(.*)' - find three digits found by spaces

replace with '$1,$2,' which adds spaces

select bunch of spaces with y '\s{4,}Y,' and replace with  ',Y' in order to make the , in front

find each row without Y  ',$' and replace with ',N'
