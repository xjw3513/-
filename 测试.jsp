<%@ page language="java"  contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.io.BufferedReader,java.io.File,java.io.FileNotFoundException,
java.io.FileReader,java.io.IOException,java.util.ArrayList,java.util.List"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body> 
<% 
File csv = new File(
		"D:\\JAVAEE\\大作业\\WebContent\\课设\\交互设计.csv"); // CSV文件路径
BufferedReader br = null;
try {
	br = new BufferedReader(new FileReader(csv));
} catch (FileNotFoundException e) {
	e.printStackTrace();
}
String line = "";
String everyLine = "";
try {
	List<String> allString = new ArrayList<>();
	while ((line = br.readLine()) != null) // 读取到的内容给line变量
	{
		everyLine = line;
		//System.out.println(everyLine);
		allString.add(everyLine);
	}
	System.out.println(allString.get(0));
	System.out.println("csv表格中所有行数：" + allString.size());
} catch (IOException e) {
	e.printStackTrace();
}

  
 
%> 
 
</body>
</html>