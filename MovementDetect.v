module MovementDetect
	#(parameter pixels = 64)
	#(parameter colorW = 16)
	#(parameter numMax = 10)
	(rColumn,gColumn,bColumn,DIFF);
	input [pixles:0][colorW:0]rColumn,gColumn,bColumn;
	output [colorW+numMax+2:0]DIFF;
	
	wire [pixles:0][colorW+2:0]diffs;
	
	compPixel comps[pixels:0] (rColumn,gColumn,bColumn,diffs);
	
endmodule 