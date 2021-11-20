import axios from "axios";
import https from "https";
import {urls} from "../constants";

const agent = new https.Agent({ keepAlive: true });

export const classifyImage = async (
	imageBase64,
	setClassificationResult
) => {
	try {
		const response = await axios.post(urls.CLASSIFICATION_CLASSIFY_IMAGE_URL,
			{"image_base64": imageBase64}
		)
		setClassificationResult(response.data);
	} catch (error) {
		console.log(error);
	}
}
