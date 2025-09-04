package com.example.mobilka;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        Button button = findViewById(R.id.submit_button);
        EditText email = findViewById(R.id.email);
        EditText password = findViewById(R.id.password);
        EditText repeatPassword = findViewById(R.id.repeat_password);
        TextView notificaton_area = findViewById(R.id.notification_area);


        button.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                boolean isMalpa = false;
                for(int i = 0; i<email.getText().length(); i++){
                    isMalpa = true;
                }

                if(!isMalpa) {
                    notificaton_area.setText("Nieprawidłowy adres email");
                }
                else if(!password.getText().toString().equals(repeatPassword.getText().toString())){
                    notificaton_area.setText("Hasła się różnią");
                }
                else {
                    notificaton_area.setText("Witaj " + email.getText().toString());
                }
            }
        });
    }
}