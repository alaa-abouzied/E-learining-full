import React, { useEffect, useState } from 'react'
import axios from "axios";
import {  Table } from 'react-bootstrap';
import { NavLink } from 'react-router-dom'
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import {useDocumentTitle} from "./setDocumentTitle"
import './css/CardImage.css'
import handleDelete from './DeleteCourse'
export default function MyCourses() {
  const [document_title, setDoucmentTitle] = useDocumentTitle("My Courses");
    let [courses,setCourses] = useState([]);
    function getMyCourses(){
        axios.get(`http://localhost:8000/course/rest/generics/`)
        .then((response)=>{
            setCourses(response.data);
        })
        .catch((error)=>{
        console.log(error);
        })
    }
    useEffect(()=>{
        getMyCourses(); 
    },[]);
  return (
    <div className="alert alert-light p-5 ">
      <h1  className='text-center '>My Courses </h1>
      <div className="container ">
        <div className="row g-3 mx-auto">
          {courses.map((course) => {
            return(
            <>
                <Card style={{ width: '18rem' }} className="me-3 mt-3">
                <Card.Img variant="top" src={course.course_image} className='rounded course_image' alt={course.course_name}/>
                  <Card.Body>
                    <Card.Title>Course Title:{course.course_name}</Card.Title>
                    <Card.Text  className=" mt-3">
                      <p>Course Cotegory:{course.course_category}</p>
                    </Card.Text>
                    <NavLink to={`/detail/${course.id}`} className=" btn btn-primary mb-2 me-2"> Show Details</NavLink>
                    <NavLink to='#' className=" btn btn-primary mb-2 ms-2"> Enroll</NavLink>
                    <div className="f-flex">
                    <NavLink to={`/update/${course.id}`} className=" btn btn-primary me-2"> update</NavLink>
                    <NavLink to={`/delete/${course.id}`}  className=" btn btn-danger ms-2"> delete</NavLink>
                    {/* <button onClick={handleDelete} className=" btn btn-danger ms-2">delete</button> */}
                    </div>
                    
                  </Card.Body>
                </Card>
            </>
            ); 
          })}
        </div>
      </div>
    </div>
  )
}
