package com.itheima.test_demo1;
//爬取数据

import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.net.URLConnection;
import java.util.ArrayList;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class test1 {
    public static void main(String[] args) throws IOException {
        String FamilynameNet="https://hanyu.baidu.com/shici/detail?from=kg1&highlight=&pid=0b2f26d4c0ddb3ee693fdb1137ee1b0d&srcid=51369";
        String BoyNameNet="http://www.nejiaoyu.com/nanhaiqiming/8465.html";
        String GirlNameNet="http://www.nejiaoyu.com/nvhaiqiming/7744.html";

//        爬取数据
        String s = webCrawler(FamilynameNet);
        String s1 = webCrawler(BoyNameNet);
        String s2 = webCrawler(GirlNameNet);
        System.out.println(s2);


//        通过正则表达式进行获取
          ArrayList<String> familyname=getData(s,".{4}(，|。)");
          ArrayList<String> Boyname=getData(s1,".{2}(、|。)");
          ArrayList<String> Girlname=getData(s2,".{2}(、|。)");



    }

    public  static String webCrawler(String net) throws IOException {
        StringBuilder SB=new StringBuilder();
        URL url=new URL(net);
        URLConnection conn= url.openConnection();
        InputStreamReader isr=new InputStreamReader(conn.getInputStream());
        int ch;
        while((ch=isr.read())!=-1){
            SB.append((char)ch);
        }
        isr.close();
        return SB.toString();
    }
    public static ArrayList<String> getData(String s,String st){
        ArrayList<String> list=new ArrayList<>();
        Pattern compile = Pattern.compile(st);
        Matcher matcher = compile.matcher(s);
        while(matcher.find()){
            String group = matcher.group();
            list.add(group);
            System.out.println(group);
        }
        return list;
    }
}
