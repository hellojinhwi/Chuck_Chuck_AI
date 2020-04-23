package running.PI.configuration;

import org.apache.http.HttpHost;
import org.elasticsearch.client.RestClient;
import org.elasticsearch.client.RestHighLevelClient;
import org.springframework.context.annotation.Configuration;
import org.springframework.stereotype.Component;

@Configuration
@Component
public class ESConfig {
	
	
	public RestHighLevelClient createConnection() {
		System.out.println("Connect OK");
		return new RestHighLevelClient(RestClient.builder(new HttpHost("127.0.0.1", 9200, "http")));
	}
}
