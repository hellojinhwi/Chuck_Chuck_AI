package running;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.ComponentScan;

@SpringBootApplication
@EnableAutoConfiguration
@ComponentScan({"running.PI.controller", "running.PI.configuration", "running.PI.model", "running.PI.service"})
public class PillIdentifierApplication {

	public static void main(String[] args) {
		SpringApplication.run(PillIdentifierApplication.class, args);
	}

}
