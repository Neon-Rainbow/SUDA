class Student{
	def __init__(self,name,age,score){
		self.name=name
		self.age=age
		self.score=score
	}
	
	def add_score(self,score){
		self.score=self.score+score
	}
		
	def print_info(self){
		print(self.name,self.age)
	}
}

a=Student('xiaoming',12,20)
a.add_score(60)
a.print_info()