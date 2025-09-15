package com.example.mobilka;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        getSupportActionBar().hide();
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        Button pralkaBtn = findViewById(R.id.pralkaBtn);
        EditText pralkaEt = findViewById(R.id.pralkaEt);
        TextView pralkaTv = findViewById(R.id.pralkaTv);
        Button odkurzaczBtn = findViewById(R.id.odkurzaczBtn);
        TextView odkurzaczTv = findViewById(R.id.odkurzaczTv);

        pralkaBtn.setOnClickListener(v -> {
            int nrPrania = -1;
            if (!pralkaEt.getText().toString().isEmpty()) {
                nrPrania = Integer.parseInt(pralkaEt.getText().toString());
            }

            if ( nrPrania >= 0  && nrPrania <= 12 ) {
                pralkaTv.setText("Numer prania: " + nrPrania);
            }
        });

        odkurzaczBtn.setOnClickListener(v -> {
            if (odkurzaczBtn.getText().toString().equals("włącz")) {
                odkurzaczBtn.setText("wyłącz");
                odkurzaczTv.setText("Odkurzacz włączony");
            }
            else {
                odkurzaczBtn.setText("włącz");
                odkurzaczTv.setText("Odkurzacz wyłączony");
            }
        });

    }
}