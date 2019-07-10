package cs2901.utec.chat_mobile;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class EventsActivity extends AppCompatActivity {

    RecyclerView mRecyclerView;
    RecyclerView.Adapter mAdapter;
    String championship_id;

    public Activity getActivity(){
        return this;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_message);
        String title = getIntent().getExtras().get("title").toString();
        championship_id = getIntent().getExtras().get("championship_id").toString();
        String category = getIntent().getExtras().get("category").toString();
        String description = getIntent().getExtras().get("description").toString();
        String endDate = getIntent().getExtras().get("endDate").toString();
        String location = getIntent().getExtras().get("location").toString();
        String price = getIntent().getExtras().get("price").toString();
        String startDate = getIntent().getExtras().get("startDate").toString();
        setTitle(title);
        mRecyclerView = findViewById(R.id.main_recycler_view);


        final TextView textViewTitle = (TextView)findViewById(R.id.title);
        final TextView textViewCategory = (TextView)findViewById(R.id.category);
        final TextView textViewDescription = (TextView)findViewById(R.id.description);
        final TextView textViewEndDate = (TextView)findViewById(R.id.endDate);
        final TextView textViewStartDate = (TextView)findViewById(R.id.startDate);
        final TextView textViewLocation = (TextView)findViewById(R.id.location);
        final TextView textViewPrice = (TextView)findViewById(R.id.price);


        textViewTitle.setText(title);
        textViewCategory.setText(category);
        textViewDescription.setText(description);
        textViewEndDate.setText(endDate);
        textViewStartDate.setText(startDate);
        textViewLocation.setText(location);
        textViewPrice.setText(price);


    }


    public void onBtnInscription(View v) {
        Intent intent = new Intent(this, InscripcionActivity.class);
        intent.putExtra("championship_id", championship_id);
        startActivity(intent);
    }


/*
    public void getChats(){
        final String userFromId = getIntent().getExtras().get("user_from_id").toString();
        String userToId = getIntent().getExtras().get("user_to_id").toString();
        String url = "http://10.0.2.2:8080/mobile/chat/getConversation/<user_from_id>/and/<user_to_id>";
        url = url.replace("<user_from_id>", userFromId);
        url = url.replace("<user_to_id>", userToId);
        RequestQueue queue = Volley.newRequestQueue(this);

        JsonObjectRequest request = new JsonObjectRequest(
                Request.Method.GET,
                url,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            JSONArray data = response.getJSONArray("response");
                            int uID = Integer.parseInt(userFromId);
                            mAdapter = new MyMessageAdapter(data, getActivity(), uID);
                            mRecyclerView.setAdapter(mAdapter);
                            mRecyclerView.smoothScrollToPosition(mRecyclerView.getAdapter().getItemCount());
                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        error.printStackTrace();
                    }
                }
        );
        queue.add(request);
    }

    public void postInscription(){
        String url = "http://10.0.2.2:8080/newMesssage";
        RequestQueue queue = Volley.newRequestQueue(this);
        Map<String, String> params = new HashMap();
        final String user_from_id = getIntent().getExtras().get("user_from_id").toString();
        final String user_to_id = getIntent().getExtras().get("user_to_id").toString();
        final String content = ((EditText)findViewById(R.id.txtMessage)).getText().toString();
        params.put("content", content);
        params.put("user_from_id",user_from_id);
        params.put("user_to_id", user_to_id);
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
        EditText editTextSend = (EditText)findViewById(R.id.txtMessage);
        editTextSend.setText("");
    }
    */
}
