package running.PI.model.DAO;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.elasticsearch.ElasticsearchException;
import org.elasticsearch.action.search.SearchRequest;
import org.elasticsearch.action.search.SearchResponse;
import org.elasticsearch.client.RequestOptions;
import org.elasticsearch.client.RestHighLevelClient;
import org.elasticsearch.index.query.BoolQueryBuilder;
import org.elasticsearch.index.query.MatchQueryBuilder;
import org.elasticsearch.index.query.MultiMatchQueryBuilder;
import org.elasticsearch.index.query.QueryBuilders;
import org.elasticsearch.search.builder.SearchSourceBuilder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import running.PI.configuration.ESConfig;
import running.PI.model.DTO.PIDTO;

//Imports the Google Cloud client library
import com.google.cloud.texttospeech.v1.AudioConfig;
import com.google.cloud.texttospeech.v1.AudioEncoding;
import com.google.cloud.texttospeech.v1.SsmlVoiceGender;
import com.google.cloud.texttospeech.v1.SynthesisInput;
import com.google.cloud.texttospeech.v1.SynthesizeSpeechResponse;
import com.google.cloud.texttospeech.v1.TextToSpeechClient;
import com.google.cloud.texttospeech.v1.VoiceSelectionParams;
import com.google.protobuf.ByteString;
import java.io.FileOutputStream;
import java.io.OutputStream;


@Component
public class PIDAO {

   @Autowired
   private ESConfig esConfig;

   public List<PIDTO> textSearch(String name, String print1, String print2, String shape, String color) throws IOException, ElasticsearchException {

      SearchRequest searchRequest = new SearchRequest("chuck");
      SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
      
      BoolQueryBuilder boolquery = QueryBuilders.boolQuery();
      
      MatchQueryBuilder inputName = QueryBuilders.matchQuery("ITEM_NAME.edge_ngram", name);
      MultiMatchQueryBuilder inputPrint1 = QueryBuilders.multiMatchQuery(print1, "PRINT_FRONT", "PRINT_BACK");
      MultiMatchQueryBuilder inputPrint2 = QueryBuilders.multiMatchQuery(print2, "PRINT_FRONT", "PRINT_BACK");
      MatchQueryBuilder inputShape = QueryBuilders.matchQuery("DRUG_SHAPE", shape);
      MatchQueryBuilder inputColor = QueryBuilders.matchQuery("COLOR_CLASS1", color);
      
      if(name != "") {
         boolquery = boolquery.must(inputName);
      } else {
         boolquery = boolquery.should(inputName);
      }
      
      if(print1 != "") {
         boolquery = boolquery.must(inputPrint1);
      } else {
         boolquery = boolquery.should(inputPrint1);
      }
      
      if(print2 != "") {
         boolquery = boolquery.must(inputPrint2);
      } else {
         boolquery = boolquery.should(inputPrint2);
      }
      
      if(shape != "") {
         boolquery = boolquery.must(inputShape);
      } else {
         boolquery = boolquery.should(inputShape);
      }
      
      if(color != "") {
         boolquery = boolquery.must(inputColor);
      } else {
         boolquery = boolquery.should(inputColor);
      }
      
      searchRequest.source(searchSourceBuilder.query(boolquery).size(10));

      SearchResponse response = null;
      RestHighLevelClient client = null;
      List<PIDTO> list = new ArrayList<>();
      
      try {
         client = esConfig.createConnection();
         response = client.search(searchRequest, RequestOptions.DEFAULT);
         
         for (int i = 0; i < response.getHits().getHits().length; i++) {
            list.add(new PIDTO(response.getHits().getHits()[i].getId(),
                  response.getHits().getHits()[i].getSourceAsMap().get("ITEM_NAME"),
                  response.getHits().getHits()[i].getSourceAsMap().get("ENTP_NAME"),
                  response.getHits().getHits()[i].getSourceAsMap().get("PRINT_FRONT"),
                  response.getHits().getHits()[i].getSourceAsMap().get("PRINT_BACK"),
                  response.getHits().getHits()[i].getSourceAsMap().get("DRUG_SHAPE"),
                  response.getHits().getHits()[i].getSourceAsMap().get("COLOR_CLASS1"),
                  response.getHits().getHits()[i].getSourceAsMap().get("CLASS_NAME")));
         }
      } finally {
         client.close();
      } 
      return list;
   }
   
   // TTS 적용한 로직 -> Google API key를 받아야함.
   public List<PIDTO> imageSearch(String name) throws IOException, ElasticsearchException {

	      SearchRequest searchRequest = new SearchRequest("chuck");
	      SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();

	      searchRequest.source(searchSourceBuilder.query(QueryBuilders.matchQuery("ITEM_NAME.edge_ngram", name)).size(1));

	      SearchResponse response = null;
	      RestHighLevelClient client = null;
	      List<PIDTO> list = new ArrayList<>();
	      List<String> sound = new ArrayList<>();
	      
	      try {
	         client = esConfig.createConnection();
	         response = client.search(searchRequest, RequestOptions.DEFAULT);
	         TextToSpeechClient textToSpeechClient = TextToSpeechClient.create();
	         
	            list.add(new PIDTO(response.getHits().getHits()[0].getId(),
	                  response.getHits().getHits()[0].getSourceAsMap().get("ITEM_NAME"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("ENTP_NAME"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("PRINT_FRONT"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("PRINT_BACK"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("DRUG_SHAPE"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("COLOR_CLASS1"),
	                  response.getHits().getHits()[0].getSourceAsMap().get("CLASS_NAME")));
	            
	            sound.add((String) response.getHits().getHits()[0].getSourceAsMap().get("ITEM_NAME"));
	            sound.add((String) response.getHits().getHits()[0].getSourceAsMap().get("ENTP_NAME"));
	            sound.add((String) response.getHits().getHits()[0].getSourceAsMap().get("PRINT_FRONT"));
	            sound.add((String) response.getHits().getHits()[0].getSourceAsMap().get("COLOR_CLASS1"));
	            
	            String para = "";
	            para += "제품명"+sound.get(0)+" ";
	            para += "회사명"+sound.get(1)+" ";
	            para += "식별문자"+sound.get(2)+" ";
	            para += "색깔"+sound.get(3)+" ";
	            
	            SynthesisInput input = SynthesisInput.newBuilder().setText(para).build();
	            VoiceSelectionParams voice = VoiceSelectionParams.newBuilder().setLanguageCode("ko-kr")
	                  .setSsmlGender(SsmlVoiceGender.NEUTRAL).build();

	            AudioConfig audioConfig = AudioConfig.newBuilder().setAudioEncoding(AudioEncoding.MP3).build();
	            SynthesizeSpeechResponse TTSresponse = textToSpeechClient.synthesizeSpeech(input, voice, audioConfig);
	            ByteString audioContents = TTSresponse.getAudioContent();

	            try (OutputStream out = new FileOutputStream("..\\ChuckChuck\\pillIdentifier\\target\\classes\\static\\assets\\audio\\output.mp3")) {
	               out.write(audioContents.toByteArray());
	               System.out.println("Audio content written to file \"output.mp3\"");
	            }
	            
	      } finally {
	         client.close();
	      } 
	      return list;
	   }
   
// TTS 적용안한 로직
//   public List<PIDTO> imageSearch(String name) throws IOException, ElasticsearchException {
//
//      SearchRequest searchRequest = new SearchRequest("chuck");
//      SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
//
//      searchRequest.source(searchSourceBuilder.query(QueryBuilders.matchQuery("ITEM_NAME.edge_ngram", name)).size(1));
//
//      SearchResponse response = null;
//      RestHighLevelClient client = null;
//      List<PIDTO> list = new ArrayList<>();
//      
//      try {
//         client = esConfig.createConnection();
//         response = client.search(searchRequest, RequestOptions.DEFAULT);
//         
//            list.add(new PIDTO(response.getHits().getHits()[0].getId(),
//                  response.getHits().getHits()[0].getSourceAsMap().get("ITEM_NAME"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("ENTP_NAME"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("PRINT_FRONT"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("PRINT_BACK"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("DRUG_SHAPE"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("COLOR_CLASS1"),
//                  response.getHits().getHits()[0].getSourceAsMap().get("CLASS_NAME")));
//      } finally {
//         client.close();
//      } 
//      return list;
//   }
   // 자동완성기능에 필요한 제품명을 가져오는 메소드
   public Object getAutocompleteData() throws IOException {
      ArrayList<Object> itemName = new ArrayList<>();
      SearchRequest searchRequest = new SearchRequest("chuck");
      SearchSourceBuilder searchSourceBuilder = new SearchSourceBuilder();
      SearchResponse response = null;
      RestHighLevelClient client = null;

      
      for(int j = 0; j <= 21000; j+=3000) {
         searchSourceBuilder.query(QueryBuilders.matchAllQuery());
         searchSourceBuilder.from(j);
         searchSourceBuilder.size(3000);

         String[] includeFields = new String[] { "ITEM_NAME" };
         String[] excludeFields = new String[] { "ENTP_NAME", "CHART", "ITEM_IMAGE", "PRINT_FRONT", "PRINT_BACK",
               "DRUG_SHAPE", "COLOR_CLASS1", "LENG_LONG", "LENG_SHORT", "THICK", "CLASS_NAME", "ETC_OTC_NAME",
               "FORM_CODE_NAME", "ITEM_ENG_NAME" };
         searchSourceBuilder.fetchSource(includeFields, excludeFields);

         searchRequest.source(searchSourceBuilder);

         try {
            client = esConfig.createConnection();

            response = client.search(searchRequest, RequestOptions.DEFAULT);

            for (int i = 0; i < response.getHits().getHits().length; i++) {
               itemName.add(response.getHits().getHits()[i].getSourceAsMap().get("ITEM_NAME"));
            }
         }finally {
            client.close();
         }
      } 
      return itemName;
   }
}