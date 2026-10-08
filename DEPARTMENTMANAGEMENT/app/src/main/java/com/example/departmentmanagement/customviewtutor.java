package com.example.departmentmanagement;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customviewtutor extends BaseAdapter {
    String[] id,name,tpic,tphn,email,quali,exp;
    private Context context;

    public customviewtutor(Context applicationContext, String[] id, String[] name, String[] tpic, String[] tphn, String[] email, String[] quali, String[] exp) {


        this.context = applicationContext;
        this.id = id;
        this.name = name;
        this.tpic = tpic;
        this.tphn = tphn;
        this.email = email;
        this.quali = quali;
        this.exp = exp;

    }

//    public customviewtutor(Context applicationContext, String[] id, String[] tpic, String[] tphn, String[] email, String[] name, String[] quali, String[] exp) {
//        this.context = applicationContext;
//        this.id = id;
//        this.name = name;
//        this.tpic = tpic;
//        this.tphn = tphn;
//        this.email = email;
//        this.quali = quali;
//        this.exp = exp;
//
//    }


    @Override
    public int getCount(  ) {
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
            gridView=inflator.inflate(R.layout.activity_customviewtutor,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView74);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView78);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView76);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView80);
        TextView tv5=(TextView)gridView.findViewById(R.id.textView83);
        ImageView im=(ImageView) gridView.findViewById(R.id.imageView8);



        tv1.setTextColor(Color.BLACK);


        tv1.setText(name[i]);
        tv2.setText(email[i]);
        tv3.setText(tphn[i]);
        tv4.setText(exp[i]);
        tv5.setText(quali[i]);


        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");
        Picasso.with(context).load(url+tpic[i]). into(im);



        return gridView;

    }
}