import React, {useState} from 'react';
import ReactDOM from 'react-dom';
import {classifyImage} from '../data';
import ClassificationResults from "../components/classification_results";

const onImageChange = (event, setClassificationResult, setBase64) => {
	if (event.target.files && event.target.files[0]) {
		let reader = new FileReader();

		reader.onload = (upload) => {
			setBase64(upload.target.result);
			classifyImage(upload.target.result, setClassificationResult);
		}

	  let img = event.target.files[0];
	  reader.readAsDataURL(img);
	}
};

const Classification = () => {

	const [classificationResult, setClassificationResult] = useState(null);
	const [base64, setBase64] = useState(null);

  return (
  <div>
  	<h1> Classification with Deep Learning </h1>
  	<p> Deep learning techniques allows the classification of images using convolutional neural networks. </p>
  	<p> In this example, you will upload a photo or take a picture with your device, and we will classificate your picture </p>
    <div>
      <input type="file" name="myImage" onChange={(evt) => onImageChange(evt, setClassificationResult, setBase64)} />
    </div>
    {base64 && <img src={base64} alt="uploaded image" height="400" width="400" />}
    {classificationResult && <ClassificationResults results={classificationResult} />}
  </div>
  );
}

export default Classification;