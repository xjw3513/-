<%@ page language="java" contentType="text/html; charset=utf-8"%>
<%@ page import="java.sql.*" %>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Insert title here</title>
	</head>
	<body>
	<table>
		<%
			Class.forName("com.microsoft.sqlserver.jdbc.SQLServerDriver");
			String url="jdbc:sqlserver://localhost:1433;DatabaseName=课设";
			String user = "sa", password="123";
			Connection conn= DriverManager.getConnection(url,user,password);
			String name= request.getParameter("name");
			String sql = "select * from job where companyFullName like '%" + name + "%'";
			Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
        %>
        <table align="center" border="1">
		<tr>
			<th>公司名称</th>
			<th>工作</th>
			<th>月薪</th>
			<th>所在城市</th>
			<th>学历要求</th>
			<th>经验要求</th>
			<th>能力要求</th>
			<th>公司规模</th>
			<th>融资情况</th>
			<th>福利待遇</th>
		</tr>
		<%
			while (rs.next()) {
		%>
		<tr>
			<td><%=rs.getString("companyFullName")%></td>
			<td><%=rs.getString("positionName")%></td>
			<td><%=rs.getString("salary")%></td>
			<td><%=rs.getString("city")%></td>
			<td><%=rs.getString("education")%></td>
			<td><%=rs.getString("workYear")%></td>
			<td><%=rs.getString("positionLables")%></td>
			<td><%=rs.getString("companySize")%></td>
			<td><%=rs.getString("financeStage")%></td>
			<td><%=rs.getString("companyLabelList")%></td>
		</tr>
        <%
            } // end for while(rs.next())
		%>
		<tr>
			<td colspan=4 align="center"><input type="submit" name="submit" value="返回"> </td>
		</tr>
		<%
            rs.close();
            stmt.close();
            conn.close();
        %>
	</table>
	</body>
</html>