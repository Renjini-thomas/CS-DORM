package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class customcomplaint extends BaseAdapter {
    String[] id,ti,dis,date,reply,replyd;
    private Context context;


    public customcomplaint(Context applicationContext, String[] id, String[] ti, String[] dis, String[] date, String[] reply, String[] replyd) {
        this.context= applicationContext;
        this.id=id;
        this.ti=ti;
        this.dis=dis;
        this.date=date;
        this.reply=reply;
        this.replyd=replyd;
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
            gridView=inflator.inflate(R.layout.activity_customcomplaint,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView50);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView52);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView54);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView56);
        TextView tv5=(TextView)gridView.findViewById(R.id.textView58);
        //ImageView im=(ImageView) gridView.findViewById(R.id.imageView);

        tv1.setTextColor(Color.BLACK);


        tv1.setText(ti[i]);
        tv2.setText(dis[i]);
        tv3.setText(date[i]);
        tv4.setText(reply[i]);
        tv5.setText(replyd[i]);



        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        //Picasso.with(context).load(url+ep[i]). into(im);

        return gridView;
    }
}