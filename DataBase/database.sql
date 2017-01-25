CREATE TABLE QnA(
	Question_id 		int Primary key,
    Question_type 		Varchar(25),
	Question_Catagory	Varchar(30),
    Question 			varchar(250),
    Anwser1				varchar(200),
    Anwser2				varchar(200),
    Anwser3				varchar(200),
    Correct_anwser		varchar(200)
);

CREATE TABLE Score(
    ID int UNIQUE Primary key,
    Name varchar(15),
    Score int
);
    
	
	