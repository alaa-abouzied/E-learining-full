import React, { useState, useEffect } from 'react';
import axios from "axios";
import Form from 'react-bootstrap/Form';

function AddCourse(){
  
    const [cats,setCats]=useState([]);
    const [data,setData]=useState({
      course_name:"",
      course_description:"",
      course_rate:"",
      course_image:"",
      course_category:"",
      course_instructor:"",
      student_course_name:""
    })
    
    const [file, setFile] = useState();
    const handleFileChange=(event)=>{
      setData({
        ...data,
        [event.target.name]:event.target.files[0]
      })
      setFile(URL.createObjectURL(event.target.files[0]));
    };


    function submit(e){
      e.preventDefault();
      axios.post("http://localhost:8000/course/rest/generics/",{
        course_name:data.course_name,
        course_description:data.course_description,
        course_rate:data.course_rate,
        course_image:e.target.course_image.files[0],
        //course_image:data.course_image.name,
        course_category:data.course_category,
        course_instructor:data.course_instructor,
        student_course_name:data.student_course_name
      },{headers:{
        'content-type':'multipart/form-data',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
      }})
      .then(res=>{console.log(res.data);})
    }

    function handle(e){
        const newdata={...data}
        newdata[e.target.name]= e.target.value
        setData(newdata)
        console.log(newdata);
    }
    
    useEffect(()=>{
        try{
          axios.get("http://localhost:8000/category/list/")
          .then((res)=>{
            setCats(res.data)
            console.log("yaraaaaaaaaaaaab:",res.data);
          });
        }catch(error){
          console.log(error);
        }
      },[]);

return(
 
  <div className='container mt-4 w-75'>
      <div className='bg-secondary'> <h1>Add New Course</h1></div>
      <Form onSubmit={(e)=>submit(e)}>
        <Form.Group className="  my-3 " >
          <Form.Label className='float-start'><h5>Course Title:</h5></Form.Label>
          <Form.Control  type="text"   name="course_name"value={data.course_name} onChange={(e)=>handle(e)}/>
        
        </Form.Group>

        <Form.Group className="mb-3 " >
          <Form.Label className='float-start'><h5>Course Description:</h5></Form.Label>
          <Form.Control  type="textarea"  value={data.course_description} name="course_description" onChange={(e)=>handle(e)}/>
        </Form.Group>

        <Form.Group className="mb-3 " >
          <Form.Label className='float-start'><h5>Course Rate:</h5></Form.Label>
          <Form.Control  type="number" value={data.course_rate} name="course_rate" onChange={(e)=>handle(e)}/>
        </Form.Group>

        <Form.Group className="mb-3" >
          <Form.Label className='float-start' name="cat_name"><h5>Course Category:</h5></Form.Label>
          <Form.Select aria-label="Default select example" value={data.course_category} name="course_category" id="category" onChange={(e)=>handle(e)}>
            {cats.map((category,index)=>{return <option key={index} value={category.id}>{category.cat_name}</option>})}
          </Form.Select>
        </Form.Group>

        <Form.Group className="mb-3 ms-0" >
          <Form.Label className='float-start'><h5>Course Image:</h5></Form.Label>
          <Form.Control  type="file" accept="image/*" name="course_image" onChange={handleFileChange} />
          <img src={file} className='inputimg'/>
        </Form.Group>

   
        <Form.Group className="mb-3 mt-1" >
          <Form.Label className='float-start'><h5>Course Instructor:</h5></Form.Label>
          <Form.Control  type="text"value={data.course_instructor} name="course_instructor" onChange={(e)=>handle(e)}/>
        </Form.Group>

        <Form.Group className="mb-3 mt-1" >
          <Form.Label className='float-start'><h5>Course student:</h5></Form.Label>
          <Form.Control  type="text"value={data.student_course_name} name="student_course_name" onChange={(e)=>handle(e)}/>
        </Form.Group>
        <button>submit</button>
      </Form>
    </div>
);
}
export default AddCourse;