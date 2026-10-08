package com.example.departmentmanagement;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.net.Uri;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.squareup.picasso.Picasso;

public class Customviewnotification extends BaseAdapter {
    String[] id,ti,di,da,lin;
    private Context context;

    public Customviewnotification(Context applicationContext, String[] id, String[] ti, String[] di, String[] da, String[] lin) {
        this.context = applicationContext;
        this.id = id;
        this.ti = ti;
        this.di = di;
        this.da = da;
        this.lin = lin;
    }

    //public Customviewnotification(Context applicationContext, String[] id, String[] tpic, String[] tphn, String[] tdesg) {
    //}


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
            gridView=inflator.inflate(R.layout.activity_customviewnotification,null);

        }
        else
        {
            gridView=(View)view;

        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView22);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView24);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView23);
        TextView tv4=(TextView)gridView.findViewById(R.id.textView25);


        tv1.setTextColor(Color.BLACK);


        tv1.setText(ti[i]);
        tv2.setText(di[i]);
        tv3.setText(da[i]);
        tv4.setText(lin[i]);
        tv4.setTag(i);
        tv4.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int pos = (int) view.getTag();
                SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
                String url=sh.getString("url","");
                String value=lin[pos];
                try {
                    Intent intent=new Intent(Intent.ACTION_VIEW, Uri.parse(value));
                    intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                    context.startActivity(intent);
                }
                catch (Exception e){
                    Toast.makeText(context, "Invalid Link", Toast.LENGTH_SHORT).show();
                }
            }
        });



        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(context);
        String url=sh.getString("url","");

        //Picasso.with(context).load(url+ep[i]). into(im);

        return gridView;

    }
}