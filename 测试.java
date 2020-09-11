import java.io.*;
import jxl.*;
public class ReadExcel
{
public static void main(String[] args)
{
try{
Workbook book=Workbook.getWorkbook(new File("D:\\JAVAEE\\大作业\\WebContent\\课设\\拉勾750条家教.xlsx"));
//获得第一个工作表对象
Sheet sheet=book.getSheet(0);
//得到第2行第1列的单元格
Cell cell1=sheet.getCell(0,1);
String result=cell1.getContents();
System.out.println(result);
book.close();
}
catch(Exception e){
System.out.println(e);
}
}
}