CREATE TABLE QnA(
	Question_id 		int UNIQUE Primary key,
    Question_type 		Varchar(25),
    Question 			varchar(250),
    Awnser1				varchar(200),
    Awnser2				varchar(200),
    Awnser3				varchar(200),
    Correct_awnser		varchar(200)
);

CREATE TABLE Score(
    ID int UNIQUE Primary key,
    Name varchar(15),
    Score int
);
    
	
	