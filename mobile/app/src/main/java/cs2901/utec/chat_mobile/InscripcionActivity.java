package cs2901.utec.chat_mobile;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class InscripcionActivity extends AppCompatActivity implements View.OnClickListener{

    Spinner tipo_de_vela_spinner;
    EditText numeroDeVela;
    Button realizarInscripcion;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inscripcion);

        tipo_de_vela_spinner = (Spinner)findViewById(R.id.spinner);
        ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.tipo_de_vela, android.R.layout.simple_spinner_item);
        tipo_de_vela_spinner.setAdapter(adapter);

        numeroDeVela = findViewById(R.id.et_numero_de_vela);
        realizarInscripcion = findViewById(R.id.buttonRealizarInscripcion);

        realizarInscripcion.setOnClickListener(new View.OnClickListener() {
            public void onClick(View v) {
                AlertDialog.Builder builder1 = new AlertDialog.Builder(InscripcionActivity.this);

                builder1.setMessage("¿Estás seguro que deseas realizar la inscripción?");
                builder1.setCancelable(true);



                builder1.setPositiveButton(
                        "Yes",
                        new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int id) {
                                postInscription();
                                dialog.cancel();

                                AlertDialog.Builder builder2 = new AlertDialog.Builder(InscripcionActivity.this);
                                builder2.setMessage("Inscripción realizada correctamente.");
                                builder2.setCancelable(false);

                                builder2.setPositiveButton(
                                        "OK",
                                        new DialogInterface.OnClickListener() {
                                            public void onClick(DialogInterface dialog, int id) {
                                                dialog.cancel();
                                            }
                                        });
                                AlertDialog alert12 = builder2.create();
                                alert12.show();

                            }
                        });



                builder1.setNegativeButton(
                        "No",
                        new DialogInterface.OnClickListener() {
                            public void onClick(DialogInterface dialog, int id) {
                                dialog.cancel();
                            }
                        });

                AlertDialog alert11 = builder1.create();
                alert11.show();
            }
        });

    }





    public void postInscription(){
        EditText txtVela = (EditText) findViewById(R.id.et_numero_de_vela);
        //EditText txtPassword = (EditText) findViewById(R.id.spinner);
        String vela = txtVela.getText().toString();
        //String password = txtPassword.getText().toString();

        final String championship_id = getIntent().getExtras().get("championship_id").toString();


        String url = "http://18.228.148.139/mobile/loadSailData";
        RequestQueue queue = Volley.newRequestQueue(this);
        Map<String, String> params = new HashMap();


        Spinner spinner = (Spinner)findViewById(R.id.spinner);
        String category = spinner.getSelectedItem().toString();
        final String user_id  = "1";

        //final String user_id = getIntent().getExtras().get("user_id").toString();
        //final String sailingNumber = numeroDeVela.toString();
        //final String category = tipo_de_vela_spinner.toString();
        //final String championship_id = getIntent().getExtras().get("championship_id").toString();


        params.put("sailingNumber", vela);
        params.put("category", category);
        params.put("user_id", user_id);
        params.put("championship_id", championship_id);

        JSONObject parameters = new JSONObject(params);
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(
                Request.Method.POST,
                url,
                parameters,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        // TODO
                    }
                }, new Response.ErrorListener() {

            @Override
            public void onErrorResponse(VolleyError error) {
                // TODO: Handle error
                error.printStackTrace();

            }
        });
        queue.add(jsonObjectRequest);
    }



    @Override
    public void onClick(View view) {
        postInscription();
    }
}
