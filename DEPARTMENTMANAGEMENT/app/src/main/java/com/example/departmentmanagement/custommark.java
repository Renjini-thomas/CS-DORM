package com.example.departmentmanagement;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

public class custommark extends BaseAdapter {
    String[] id,mark,grade,sub;

    private final Context context;


    public custommark(Context applicationContext, String[] id, String[] mark, String[] grade, String[] sub) {
        this.context = applicationContext;
        this.id = id;
        this.mark = mark;
        this.grade= grade;
        this.sub= sub;
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
            gridView=inflator.inflate(R.layout.activity_custommark,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView86);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView88);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView59);
        //ImageView im=(ImageView) gridView.findViewById(R.id.imageView);

        tv1.setTextColor(Color.BLACK);


        tv1.setText(mark[i]);
        tv2.setText(grade[i]);
        tv3.setText(sub[i]);



        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        //Picasso.with(context).load(url+ep[i]). into(im);

        return gridView;
    }
}