package com.cxl.sys.test;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.logging.SimpleFormatter;

/**
 * Created by Administrator on 2015-03-15.
 */
public class MainTest {
    public static void main(String args[]) {
        Date date = new Date();
        System.out.print(date.getTime());
        SimpleDateFormat simpleDateFormat = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");
        System.out.print(simpleDateFormat.format(date));
    }
}
