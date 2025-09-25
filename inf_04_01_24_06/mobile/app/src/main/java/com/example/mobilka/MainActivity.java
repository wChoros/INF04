package com.example.mobilka;

import android.annotation.SuppressLint;
import android.graphics.drawable.Drawable;
import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import java.util.Random;

public class MainActivity extends AppCompatActivity {
    private int thisScore = 0;
    private int gameScore = 0;
    private int tmp = 0;
    Random rand = new Random();




    @SuppressLint("UseCompatLoadingForDrawables")
    Drawable getCube(int number) {
        switch (number){
            case 1:
                return getDrawable(R.drawable.k1);
            case 2:
                return  getDrawable(R.drawable.k2);
            case 3:
                return getDrawable(R.drawable.k3);
            case 4:
                return getDrawable(R.drawable.k4);
            case 5:
                return getDrawable(R.drawable.k5);
            case 6:
                return getDrawable(R.drawable.k6);
            default:
                return getDrawable(R.drawable.question);
        }
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        Button startGameBtn = findViewById(R.id.start_btn);
        Button resetGameBtn = findViewById(R.id.reset_btn);
        ImageView cube1 = findViewById(R.id.kosc1);
        ImageView cube2 = findViewById(R.id.kosc2);
        ImageView cube3 = findViewById(R.id.kosc3);
        ImageView cube4 = findViewById(R.id.kosc4);
        ImageView cube5 = findViewById(R.id.kosc5);

        TextView thisScoreTw = findViewById(R.id.this_score);
        TextView gameScoreTw = findViewById(R.id.game_score);


        startGameBtn.setOnClickListener(v -> {
            tmp = rand.nextInt(6) + 1;
            cube1.setImageDrawable(getCube(tmp));
            thisScore += tmp;
            gameScore += tmp;

            tmp = rand.nextInt(6) + 1;
            cube2.setImageDrawable(getCube(tmp));
            thisScore += tmp;
            gameScore += tmp;

            tmp = rand.nextInt(6) + 1;
            cube3.setImageDrawable(getCube(tmp));
            thisScore += tmp;
            gameScore += tmp;

            tmp = rand.nextInt(6) + 1;
            cube4.setImageDrawable(getCube(tmp));
            thisScore += tmp;
            gameScore += tmp;

            tmp = rand.nextInt(6) + 1;
            cube5.setImageDrawable(getCube(tmp));
            thisScore += tmp;
            gameScore += tmp;

            thisScoreTw.setText("Wynik tego losowania: " + String.valueOf(thisScore));
            gameScoreTw.setText("Wynik gry: " + String.valueOf(gameScore));
            thisScore = 0;
        });

        resetGameBtn.setOnClickListener(v -> {
            thisScore = 0;
            gameScore = 0;
            cube1.setImageDrawable(getDrawable(R.drawable.question));
            cube2.setImageDrawable(getDrawable(R.drawable.question));
            cube3.setImageDrawable(getDrawable(R.drawable.question));
            cube4.setImageDrawable(getDrawable(R.drawable.question));
            cube5.setImageDrawable(getDrawable(R.drawable.question));

            thisScoreTw.setText("Wynik tego losowania: 0");
            gameScoreTw.setText("Wynik gry: 0");
        });
    }
}