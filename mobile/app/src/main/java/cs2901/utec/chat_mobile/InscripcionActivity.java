package cs2901.utec.chat_mobile;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ListView;
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
                postMessage();
            }
        });
    }





    public void postMessage(){
        String url = "http://10.0.2.2:8080/sailing";
        RequestQueue queue = Volley.newRequestQueue(this);
        Map<String, String> params = new HashMap();


        //final String user_id = getIntent().getExtras().get("user_id").toString();
        final String user_id  = "8";
        final String sailingNumber = numeroDeVela.toString();
        final String category = tipo_de_vela_spinner.toString();
        //final String championship_id = getIntent().getExtras().get("championship_id").toString();
        final String championship_id = "4";

        params.put("user_id", user_id);
        params.put("sailingNumber", sailingNumber);
        params.put("category", category);
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
        postMessage();
    }
}