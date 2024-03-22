module compPixel
	#(parameter colorW = 16)
	(oRED, oBLUE, oGREEN,
	nRED, nBLUE, nGREEN,
	DIFF);
	input [colorW:0]oRED,oBLUE,oGREEN;
	input [colorW:0]nRED,nBLUE,nGREEN;
	output [colorW+2:0]DIFF;
	
	wire [colorW:0]rDiff,bDiff,gDiff;
	
	assign rDiff = oRED - nRED;
	assign bDiff = oBLUE - nBLUE;
	assign gDiff = oGREEN - nGREEN;
	assign DIFF = rDiff + bDiff + gDiff;

endmodule 