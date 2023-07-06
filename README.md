# VisualScript CLI - 
## A CLI for doing common computer vision tasks, fast.


VisualScript is built in Python, offering a simple syntax for running object detection, classification, and segmentation models.

It is a submodule of [vision script](https://github.com/capjamesg/visionscript)



## Installation :
``` bash
pip install git+https://github.com/mahimairaja/vscript
```

### vscript console 🚀: 

```bash 
❯ vscript --repl console
Welcome to VisualScript!
Type 'Exit[]' to exit.
Read the docs at https://visualscript.org/docs
For help, type 'Help[FunctionName]'.
--------------------
>>> Load["photo.jpg"]
>>> Detect["person"]
>>> Say[]
person 0.85 [          0      16.443      112.87      170.44]
```






## Documentation 📄

- `Load["./abbey.jpg"]` -> Load the image
- `Size[]` -> Get the size of the image
- `Say[]` -> Say the result of the last function
- `Detect["person"]` -> Detect the person
- `Replace["emoji.png"]` -> Replace the person with black image
- `Cutout[]` -> Cutout the last detections
- `Count[]` -> Count the last detections
- `CountInRegion[0, 0, 500, 500]` -> Count the last detections in the region (x1, y1, x2, y2)
- `Classify["cat", "dog"]` -> Classify the image in the provided categories
- `Save["./abbey2.jpg"]` -> Save the last image
- `Show[]` -> Show the last image
  - If you have run inference, this will plot inference results on the image with which you are working.
- `x = 1` -> Set the variable x to 1
- `True` and `False`: Booleans
- `If[Statement]`: If the statement is true, run the next line (the only value that evaluates to `False` is `False` right now so this is not yet useful).
- `x == y`: Test for equality. Check if x is equal to y.
- `In["./images"]`: Load all images in the `./images` folder


## Core Libraries Used

- CLIP
- YOLOv8
- FastSAM
- [supervision](https://github.com/roboflow/supervision)
- PIL
- Lark for lexing


### Syntax

The syntax is inspired by both Python and the Wolfram Language. VisualScript is an interpreted language, run line-by-line like Python. Statements use the format:

```
Statement[argument1, argument2, ...]
```

This is the same format as the Wolfram Language.
