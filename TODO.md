# TODO

* features from PyFeyn
	* blobs (line visible path)
	* arrows (free, parallel)
	* draft mode (turn off all 3d effects)
	* line fracpoint
	* better marker convenience
	* multiline
	* more markers
		* arrow
		* asterisk
* matplotlib style rc-file for defaults (for all lines, special lines, inheritance)
	* python code
* matplotlib/pyplot style API
* Write a manual.
* Introduce unit testing
* Allow setting initial/final straight components of decorated lines.
* Allow single lines to be deviated sharply (split?) round a vertex.
* Do hatched patterns better than PyX (or fix PyX's implementation).
* Allow tree-level diagrams to be generated automatically by minimising the
  "energy" of a specified graph topology (a la FeynMF).
* Fix pattern stroke colour problem.
* Improve multi-lines. Should be defined by number of lines and
  max-width/half-width OR number and separation. Arrows shouldn't necessarily
  be duplicated on all lines. Auto-sizing to blobs?  Should definitely crop to
  a visible path on the markers/blobs - should the visible path cropper be
  broken out as a standalone internal function?
