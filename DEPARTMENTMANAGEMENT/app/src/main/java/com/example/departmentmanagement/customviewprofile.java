package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customviewprofile extends BaseAdapter {
    String[] id,na,sp,yr,sem,dob,ad,reg,ph,add,em,gd;
    private final Context context;

    public customviewprofile(Context applicationContext, String[] id, String[] sp,String[] na, String[] yr, String[] sem, String[] dob, String[] ad, String[] reg, String[] ph,String[] add, String[] em, String[] gd) {
        this.context = applicationContext;
        this.id = id;
        this.sp = sp;
        this.na = na;
        this.yr = yr;
        this.sem = sem;
        this.dob = dob;
        this.ad = ad;
        this.reg = reg;
        this.ph = ph;
        this.add = add;
        this.em = em;
        this.gd = gd;
    }


    @Override
    public int getCount() {
        return id.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(context);
            //gridView=inflator.inflate(R.layout.customview, null);
            gridView=inflator.inflate(R.layout.activity_customviewprofile,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView30);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView32);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView34);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView36);
        TextView tv5=(TextView)gridView.findViewById(R.id.textView38);
        TextView tv6=(TextView)gridView.findViewById(R.id.textView40);
        TextView tv7=(TextView)gridView.findViewById(R.id.textView42);
        TextView tv8=(TextView)gridView.findViewById(R.id.textView46);
        TextView tv9=(TextView)gridView.findViewById(R.id.textView44);
        TextView tv10=(TextView)gridView.findViewById(R.id.textView48);
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView4);

        //Button b1 = (Button)gridView.findViewById(R.id.button7);
        Button b2 = (Button)gridView.findViewById(R.id.button9);

       // b1.setTag(i);
        b2.setTag(i);



        b2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                SharedPreferences sh  = PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor editor = sh.edit();
                editor.putString("sid",id[pos]);
                editor.apply();
                Intent in = new Intent(context,Moreinfo.class);
                in.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(in);
            }
        });


//        b1.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                int pos = (int) view.getTag();
//                SharedPreferences sh  = PreferenceManager.getDefaultSharedPreferences(context);
//                SharedPreferences.Editor editor = sh.edit();
//                editor.putString("sid",id[pos]);
//                editor.apply();
//                Intent in = new Intent(context,VIEWMARK.class);
//                in.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
//                context.startActivity(in);
//            }
//        });


        Button b = (Button)gridView.findViewById(R.id.button6);
        b.setTag(i);
        b.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                SharedPreferences sh  = PreferenceManager.getDefaultSharedPreferences(context);
                SharedPreferences.Editor editor = sh.edit();
                editor.putString("sid",id[pos]);
                editor.apply();
                Intent in = new Intent(context,VIEWSUBANDSTAFF.class);
                in.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                context.startActivity(in);
            }
        });

        tv1.setTextColor(Color.BLACK);


        tv1.setText(na[i]);
        tv2.setText(yr[i]);
        tv3.setText(sem[i]);
        tv4.setText(dob[i]);
        tv5.setText(ad[i]);
        tv6.setText(reg[i]);
        tv7.setText(ph[i]);
        tv8.setText(add[i]);
        tv9.setText(em[i]);
        tv10.setText(gd[i]);





        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        Picasso.with(context).load(url+sp[i]). into(im);

        return gridView;

    }
}