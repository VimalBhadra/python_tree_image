from sys import stdout;
import Image
import ImageFont, ImageDraw, ImageOps


class node:
	data=None;
  first=None;
	last=None;
	next=None;
	mom=None;
	child=0;
	def __init__(self,dat):
        	self.data = dat;


class tree:
	root=None;
	now=None;
	size=0;
	def __init__(self,root):
		self.root=node(root);
		self.now=self.root;
	def add(self,link,str):
		link.child+=1;
		newnode=node(str);
		if(link.first==None):
			link.first=newnode;
			link.last=newnode;
			newnode.mom=link;
		else:
			link.last.next=newnode;
			newnode.mom=link;
			link.last=newnode;
	def element(self,link):
		if(link.first==None):
			return 1;
		cou=1;curr=link.first;
		while(curr!=None):
			cou+=self.element(curr);
			curr=curr.next;
		return cou;
	def image(self):
		fontPath =  "/usr/share/fonts/truetype/didot/GFSDidotBold.otf"
		sans16  =  ImageFont.truetype ( fontPath, 20 )
		im  =  Image.new ( "RGB", (1300,800), "#ddd" )
		draw  =  ImageDraw.Draw ( im )
		def drow(link,width,px,py):
			draw.text ( (px,py), link.data, font=sans16, fill="red" );
			curr=link.first;
			cou=0;
			ele1=self.element(link)-1.0;
			while(curr!=None):
				ele=self.element(curr);
				draw.line((px,py+20,px-width/2.0 + cou + (width*ele)/(ele1*2) ,py+80), fill=(2,1,200));
				drow(curr,width*ele/ele1,px-width/2.0+cou+(width*ele)/(ele1*2) ,py+80);
				curr=curr.next;
				cou+=width*ele/ele1;


		drow(self.root,1300,650,3);
		im.save("tree.png");
		



tre=tree("");


#this function is reading string tree and converting it in a python tree data-structure
def read(str):
	now=tre.root;
	for i in range(len(str)):
		if(str[i]=='['):
			tre.add(tre.now,"");
			tre.now=tre.now.last;
		elif(str[i]==']' and tre.now.mom!=None):
			tre.now=tre.now.mom;
		else:
			if(len(tre.now.data)<10):
				tre.now.data+=str[i];
			else:
				size=len(tre.now.data);
				if(tre.now.data[size-1]!='.'):
					tre.now.data+=" ..";
	



str="435f1[44[666][saini][tinku jiya[1][2]]][222[444[mohit[1][2]][saini[1][2222][3333][44444][555]]]]";
str1="33[55[6]][33]";
read(str);
tre.image();
