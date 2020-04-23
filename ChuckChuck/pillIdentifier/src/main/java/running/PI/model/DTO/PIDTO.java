package running.PI.model.DTO;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class PIDTO {
	private Object id;
	private Object itemName;
	private Object entpName;
	private Object printFront;
	private Object printBack;
	private Object drugShape;
	private Object colorClass;
	private Object className;
	
	public PIDTO(Object itemName) {
		this.itemName = itemName;
	}
	
	@Override
	public String toString() {
		return "\"" + (String) itemName + "\"";
	}
}

