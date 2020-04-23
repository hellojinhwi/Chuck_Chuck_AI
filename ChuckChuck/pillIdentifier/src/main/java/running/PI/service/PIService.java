package running.PI.service;

import java.io.IOException;
import java.util.List;

import org.elasticsearch.ElasticsearchException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

import running.PI.model.DAO.PIDAO;
import running.PI.model.DTO.PIDTO;

@Service
@Component
public class PIService {
   
   @Autowired
   private PIDAO PIDAO;
   
   public List<PIDTO> textSearch(String name, String print1, String print2, String shape, String color) throws ElasticsearchException, IOException {
      return PIDAO.textSearch(name, print1, print2, shape, color);
   }
   
   public List<PIDTO> imageSearch(String name) throws ElasticsearchException, IOException {
      return PIDAO.imageSearch(name);
   }
   
   public  Object getAutocompleteData() throws IOException {
      return PIDAO.getAutocompleteData();
   }
}