package com.kanistyle.home.api.repository;

import com.kanistyle.home.api.entity.Hygrothermograph;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource
public interface HygrothermographRepository extends JpaRepository<Hygrothermograph, Integer> {
}
